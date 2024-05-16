#users.models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import date



class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    first_name = models.CharField(max_length=30, null=True,blank=True)
    last_name = models.CharField(max_length=30, null=True,blank=True)
    phone_number = models.CharField(max_length=20, null=True,blank=True)
    DOB = models.DateField(null=True,blank=True)
    race = models.CharField(max_length=50, null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=50, null=True,blank=True)
    emergency_contact_number = models.CharField(max_length=20, null=True,)
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True)
    address = models.CharField(max_length=200, null=True,blank=True )
    city = models.CharField(max_length=100, null=True,blank=True)
    state = models.CharField(max_length=50, null=True,blank=True)
    zip_code = models.CharField(max_length=10, null=True,blank=True)
    country = models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


        
class Student(Person):
    LEVEL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES,  null=True,blank=True)
    class_type = models.CharField(max_length=50, null=True,blank=True)
    STATUS_CHOICES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, null=True,blank=True)
    STUDENT_TYPE_CHOICES = [
        ('D', 'Domestic'),
        ('I', 'International'),
    ]
    student_type = models.CharField(max_length=1, choices=STUDENT_TYPE_CHOICES,  null=True,blank=True)
    campus = models.CharField(max_length=100,  null=True,blank=True)
    advisor = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True, blank=True, related_name='advised_students')
    major = models.ForeignKey('courses.Major', on_delete=models.SET_NULL, null=True, blank=True)
    minor = models.ForeignKey('courses.Minor', on_delete=models.SET_NULL, null=True, blank=True)
    classes_taking = models.ManyToManyField('courses.Course', related_name='students_enrolled', blank=True)
    classes_took = models.ManyToManyField('courses.Course', related_name='students_completed', blank=True)
    grades = models.JSONField(default=dict, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    credits_earned = models.IntegerField(default=0)
    expected_graduation_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def get_email(self):
        return f"{self.first_name[0]}.{self.last_name}@student.school.edu"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def set_general_info(self, level, class_type, status, student_type, campus, advisor):
        self.level = level
        self.class_type = class_type
        self.status = status
        self.student_type = student_type
        self.campus = campus
        self.advisor = advisor
        self.save()

    def set_academic_info(self, major, minor, classes_taking, classes_took, grades, gpa, credits_earned, expected_graduation_date):
        self.major = major
        self.minor = minor
        self.classes_taking.set(classes_taking)
        self.classes_took.set(classes_took)
        self.grades = grades
        self.gpa = gpa
        self.credits_earned = credits_earned
        self.expected_graduation_date = expected_graduation_date
        self.save()

    def get_age(self):
        today = date.today()
        age = today.year - self.DOB.year - ((today.month, today.day) < (self.DOB.month, self.DOB.day))
        return age

class Professor(Person):
    TITLE_CHOICES = [
        ('ASST', 'Assistant Professor'),
        ('ASSOC', 'Associate Professor'),
        ('PROF', 'Professor'),
        ('LECT', 'Lecturer'),
        ('INST', 'Instructor'),
        ('CHAIR', 'Chairman'),
    ]
    title = models.CharField(max_length=5, choices=TITLE_CHOICES, null=True, blank=True)
    department = models.ForeignKey('courses.Department', on_delete=models.SET_NULL, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    office_location = models.CharField(max_length=100,null=True, blank=True)
    office_hours = models.TextField(null=True, blank=True)
    research_interests = models.TextField(null=True, blank=True)
    website = models.URLField(blank=True,null=True)
    courses_teaching = models.ManyToManyField('courses.Course', related_name='professors', blank=True, null=True)

    def get_email(self):
        return f"{self.first_name[0]}.{self.last_name}@faculty.school.edu"

    def get_full_name(self):
        return f"{self.title} {self.first_name} {self.last_name}"