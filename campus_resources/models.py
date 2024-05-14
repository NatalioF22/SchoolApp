from django.db import models
from django.contrib.auth.models import User

class LibraryItem(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    availability_status = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Book(LibraryItem):
    isbn = models.CharField(max_length=20)

class Journal(LibraryItem):
    publisher = models.CharField(max_length=100)
    issn = models.CharField(max_length=20)

class StudySpace(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    amenities = models.TextField()
    availability = models.BooleanField(default=True)

class TutoringService(models.Model):
    subject_area = models.CharField(max_length=100)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    availability = models.TextField()
    location = models.CharField(max_length=100)

class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    application_deadline = models.DateField()

class CareerEvent(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()

class StudentOrganization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    contact_email = models.EmailField()

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

class Bus(models.Model):
    route_number = models.CharField(max_length=20)
    stops = models.TextField()
    timings = models.TextField()

class Building(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    description = models.TextField()