from django.db import models
from django.core.exceptions import ValidationError

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    chairperson = models.ForeignKey('users.Professor', on_delete=models.SET_NULL, null=True, blank=True, related_name='department_chaired')

    def __str__(self):
        return self.name

    def get_courses(self):
        return self.course_set.all()

    def get_professors(self):
        return self.professor_set.all()

    def get_majors(self):
        majors = []
        for course in self.get_courses():
            majors.extend(course.majors_core.all())
            majors.extend(course.majors_required.all())
        return set(majors)

    def clean(self):
        if self.chairperson and self.chairperson.title != 'CHAIR':
            raise ValidationError("Only professors with the title 'Chairman' can be assigned as the chairperson.")

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    credits = models.IntegerField()
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Major(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    minimum_credits = models.IntegerField(default=120)
    core_courses = models.ManyToManyField(Course, related_name='majors_core')
    required_courses = models.ManyToManyField(Course, related_name='majors_required')
    core_skills = models.ManyToManyField(Course, related_name='majors_core_skills')
    core_seminars = models.ManyToManyField(Course, related_name='majors_core_seminars')
    core_writing_speaking_intensive = models.ManyToManyField(Course, related_name='majors_core_writing_speaking_intensive')
    core_distribution = models.ManyToManyField(Course, related_name='majors_core_distribution')
    core_additional_distribution = models.ManyToManyField(Course, related_name='majors_core_additional_distribution')
    program_requirements = models.ManyToManyField(Course, related_name='majors_program_requirements')

    def __str__(self):
        return self.name

    def get_total_credits(self):
        total_credits = 0
        for course in self.core_courses.all():
            total_credits += course.credits
        for course in self.required_courses.all():
            total_credits += course.credits
        return total_credits

    def is_requirements_met(self, student):
        core_courses_taken = student.classes_took.filter(majors_core=self)
        required_courses_taken = student.classes_took.filter(majors_required=self)
        core_skills_taken = student.classes_took.filter(majors_core_skills=self)
        core_seminars_taken = student.classes_took.filter(majors_core_seminars=self)
        core_writing_speaking_intensive_taken = student.classes_took.filter(majors_core_writing_speaking_intensive=self)
        core_distribution_taken = student.classes_took.filter(majors_core_distribution=self)
        core_additional_distribution_taken = student.classes_took.filter(majors_core_additional_distribution=self)
        program_requirements_taken = student.classes_took.filter(majors_program_requirements=self)

        if (
            core_courses_taken.count() == self.core_courses.count() and
            required_courses_taken.count() == self.required_courses.count() and
            core_skills_taken.count() == self.core_skills.count() and
            core_seminars_taken.count() == self.core_seminars.count() and
            core_writing_speaking_intensive_taken.count() == self.core_writing_speaking_intensive.count() and
            core_distribution_taken.count() == self.core_distribution.count() and
            core_additional_distribution_taken.count() == self.core_additional_distribution.count() and
            program_requirements_taken.count() == self.program_requirements.count()
        ):
            return True
        return False

class Minor(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True) 
    description = models.TextField()
    minimum_credits = models.IntegerField(default=18)
    required_courses = models.ManyToManyField(Course, related_name='minors_required')

    def __str__(self):
        return self.name

    def get_total_credits(self):
        total_credits = 0
        for course in self.required_courses.all():
            total_credits += course.credits
        return total_credits

    def is_requirements_met(self, student):
        required_courses_taken = student.classes_took.filter(minors_required=self)

        if required_courses_taken.count() == self.required_courses.count():
            return True
        return False