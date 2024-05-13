from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('professor', 'Professor'),
        ('student', 'Student'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    # Add related_name attributes to groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set",  # Changed related_name
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",  # Changed related_name
        related_query_name="user_permission",
    )

    def __str__(self):
        return self.username


# Rest of the models (Professor, Student, Classes) remain the same
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    DOB = models.DateField()
    race = models.CharField(max_length=50)
    emergency_contact_name = models.CharField(max_length=50)
    emergency_contact_number = models.CharField(max_length=20)
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    level = models.CharField(max_length=50, null=True, blank=True)
    class_type = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    student_type = models.CharField(max_length=50, null=True, blank=True)
    campus = models.CharField(max_length=100, null=True, blank=True)
    advisor = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True, blank=True, related_name='advised_students')
    classes_taking = models.JSONField(default=list, blank=True)
    classes_took = models.JSONField(default=list, blank=True)
    grades = models.JSONField(default=list, blank=True)

    def get_email(self):
        return f"{self.first_name[0]}.{self.last_name}@student.school.edu"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def setGeneralInfo(self, level, class_type, status, student_type, campus, advisor):
        self.level = level
        self.class_type = class_type
        self.status = status
        self.student_type = student_type
        self.campus = campus
        self.advisor = advisor
        self.save()

    def setAdacemicInfo(self, classes_taking, classes_took, grades):
        self.classes_taking = classes_taking
        self.classes_took = classes_took
        self.grades = grades
        self.save()

class Professor(Person):
    STATUS_CHOICES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='professor', null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    professor_type = models.CharField(max_length=50)
    classes_taught = models.JSONField(default=list, blank=True)
    classes_teaching = models.ManyToManyField('Subject', blank=True, related_name='professors')

    def get_email(self):
        return f"{self.first_name[0]}.{self.last_name}@staff.school.edu"

    def setGeneralInfo(self, status, professor_type):
        self.status = status
        self.professor_type = professor_type
        self.save()

    def setAdacemicInfo(self, classes_taught):
        self.classes_taught = classes_taught
        self.save()

    def assign_student(self, student):
        if student not in self.advised_students.all():
            self.advised_students.add(student)
            self.save()
        else:
            print(f"This student '{student.get_full_name()}' is already assigned to you!")

    def assign_subject(self, subject):
        if subject not in self.classes_teaching.all():
            self.classes_teaching.add(subject)
            self.save()
        else:
            print(f"This subject '{subject.title}' is already assigned to you!")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    CRN = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    credits = models.IntegerField()
    prerequisites = models.JSONField(default=list, blank=True)
    meeting_times = models.JSONField(default=list, blank=True)
    attributes = models.JSONField(default=dict, blank=True)
    students = models.ManyToManyField('Student', blank=True, related_name='classes_enrolled')
    professor = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True, blank=True, related_name='subjects_teaching')

    def __str__(self):
        return f"{self.code} - {self.title}"

    def assign_professor(self, professor):
        self.professor = professor
        self.save()

    def assign_student(self, student):
        self.students.add(student)
        self.save()

    def remove_student(self, student):
        self.students.remove(student)
        self.save()