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

class Address(models.Model):
    class USStates(models.TextChoices):
        AL = 'AL', 'Alabama'
        AK = 'AK', 'Alaska'
        AZ = 'AZ', 'Arizona'
        AR = 'AR', 'Arkansas'
        CA = 'CA', 'California'
        CO = 'CO', 'Colorado'
        CT = 'CT', 'Connecticut'
        DE = 'DE', 'Delaware'
        FL = 'FL', 'Florida'
        GA = 'GA', 'Georgia'
        HI = 'HI', 'Hawaii'
        ID = 'ID', 'Idaho'
        IL = 'IL', 'Illinois'
        IN = 'IN', 'Indiana'
        IA = 'IA', 'Iowa'
        KS = 'KS', 'Kansas'
        KY = 'KY', 'Kentucky'
        LA = 'LA', 'Louisiana'
        ME = 'ME', 'Maine'
        MD = 'MD', 'Maryland'
        MA = 'MA', 'Massachusetts'
        MI = 'MI', 'Michigan'
        MN = 'MN', 'Minnesota'
        MS = 'MS', 'Mississippi'
        MO = 'MO', 'Missouri'
        MT = 'MT', 'Montana'
        NE = 'NE', 'Nebraska'
        NV = 'NV', 'Nevada'
        NH = 'NH', 'New Hampshire'
        NJ = 'NJ', 'New Jersey'
        NM = 'NM', 'New Mexico'
        NY = 'NY', 'New York'
        NC = 'NC', 'North Carolina'
        ND = 'ND', 'North Dakota'
        OH = 'OH', 'Ohio'
        OK = 'OK', 'Oklahoma'
        OR = 'OR', 'Oregon'
        PA = 'PA', 'Pennsylvania'
        RI = 'RI', 'Rhode Island'
        SC = 'SC', 'South Carolina'
        SD = 'SD', 'South Dakota'
        TN = 'TN', 'Tennessee'
        TX = 'TX', 'Texas'
        UT = 'UT', 'Utah'
        VT = 'VT', 'Vermont'
        VA = 'VA', 'Virginia'
        WA = 'WA', 'Washington'
        WV = 'WV', 'West Virginia'
        WI = 'WI', 'Wisconsin'
        WY = 'WY', 'Wyoming'

    place = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=2, choices=USStates.choices, blank=True, null=True)
    city = models.TextField(blank=True, null=True)  # Changed City to city to follow Python naming conventions

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}"

    
# Create your models here.
class Event(models.Model):
    organizer = models.ForeignKey("users.Professor", on_delete=models.CASCADE, null=True, blank=True, related_name='organizer')
    title = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    location = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name='location')
    contact = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField( upload_to='media/', blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class Bus(models.Model):
    route_number = models.CharField(max_length=20)
    stops = models.TextField()
    timings = models.TextField()

class Building(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    description = models.TextField()