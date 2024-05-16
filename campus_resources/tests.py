from django.test import TestCase
from django.contrib.auth.models import User
from campus_resources.models import *

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_book_creation(self):
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            publication_year=2023,
            availability_status='Available',
            location='Library',
            isbn='1234567890'
        )
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.author, 'Test Author')
        self.assertEqual(book.publication_year, 2023)
        self.assertEqual(book.availability_status, 'Available')
        self.assertEqual(book.location, 'Library')
        self.assertEqual(book.isbn, '1234567890')

    def test_journal_creation(self):
        journal = Journal.objects.create(
            title='Test Journal',
            author='Test Author',
            publication_year=2023,
            availability_status='Available',
            location='Library',
            publisher='Test Publisher',
            issn='1234-5678'
        )
        self.assertEqual(journal.title, 'Test Journal')
        self.assertEqual(journal.author, 'Test Author')
        self.assertEqual(journal.publication_year, 2023)
        self.assertEqual(journal.availability_status, 'Available')
        self.assertEqual(journal.location, 'Library')
        self.assertEqual(journal.publisher, 'Test Publisher')
        self.assertEqual(journal.issn, '1234-5678')

    def test_study_space_creation(self):
        study_space = StudySpace.objects.create(
            name='Test Study Space',
            location='Library',
            capacity=50,
            amenities='Desks, Chairs, Wi-Fi',
            availability=True
        )
        self.assertEqual(study_space.name, 'Test Study Space')
        self.assertEqual(study_space.location, 'Library')
        self.assertEqual(study_space.capacity, 50)
        self.assertEqual(study_space.amenities, 'Desks, Chairs, Wi-Fi')
        self.assertTrue(study_space.availability)

    def test_tutoring_service_creation(self):
        tutoring_service = TutoringService.objects.create(
            subject_area='Mathematics',
            tutor=self.user,
            availability='Monday, Wednesday, Friday',
            location='Library'
        )
        self.assertEqual(tutoring_service.subject_area, 'Mathematics')
        self.assertEqual(tutoring_service.tutor, self.user)
        self.assertEqual(tutoring_service.availability, 'Monday, Wednesday, Friday')
        self.assertEqual(tutoring_service.location, 'Library')

    def test_job_posting_creation(self):
        job_posting = JobPosting.objects.create(
            title='Test Job',
            company='Test Company',
            location='Test Location',
            description='Test Description',
            application_deadline='2023-12-31'
        )
        self.assertEqual(job_posting.title, 'Test Job')
        self.assertEqual(job_posting.company, 'Test Company')
        self.assertEqual(job_posting.location, 'Test Location')
        self.assertEqual(job_posting.description, 'Test Description')
        self.assertEqual(str(job_posting.application_deadline), '2023-12-31')

    def test_career_event_creation(self):
        career_event = CareerEvent.objects.create(
            name='Test Career Event',
            date='2023-12-31',
            time='10:00:00',
            location='Test Location',
            description='Test Description'
        )
        self.assertEqual(career_event.name, 'Test Career Event')
        self.assertEqual(str(career_event.date), '2023-12-31')
        self.assertEqual(str(career_event.time), '10:00:00')
        self.assertEqual(career_event.location, 'Test Location')
        self.assertEqual(career_event.description, 'Test Description')

    def test_student_organization_creation(self):
        student_org = StudentOrganization.objects.create(
            name='Test Student Organization',
            description='Test Description',
            category='Test Category',
            contact_email='test@example.com'
        )
        self.assertEqual(student_org.name, 'Test Student Organization')
        self.assertEqual(student_org.description, 'Test Description')
        self.assertEqual(student_org.category, 'Test Category')
        self.assertEqual(student_org.contact_email, 'test@example.com')

    def test_address_creation(self):
        address = Address.objects.create(
            place='Test Place',
            address='Test Address',
            state='CA',
            city='Test City'
        )
        self.assertEqual(address.place, 'Test Place')
        self.assertEqual(address.address, 'Test Address')
        self.assertEqual(address.state, 'CA')
        self.assertEqual(address.city, 'Test City')
        self.assertEqual(str(address), 'Test Address, Test City, CA')

    def test_event_creation(self):
        location = Address.objects.create(city='Test City', state='CA')
        event = Event.objects.create(
            organizer=None,
            title='Test Event',
            start_date='2023-12-31',
            end_date='2024-01-01',
            price=100,
            description='Test Description',
            location=location,
            contact='Test Contact'
        )
        self.assertEqual(event.title, 'Test Event')
        self.assertEqual(str(event.start_date), '2023-12-31')
        self.assertEqual(str(event.end_date), '2024-01-01')
        self.assertEqual(event.price, 100)
        self.assertEqual(event.description, 'Test Description')
        self.assertEqual(event.location, location)
        self.assertEqual(event.contact, 'Test Contact')
        self.assertEqual(str(event), 'Test Event')

    def test_bus_creation(self):
        bus = Bus.objects.create(
            route_number='Route 1',
            stops='Stop 1, Stop 2, Stop 3',
            timings='10:00, 11:00, 12:00'
        )
        self.assertEqual(bus.route_number, 'Route 1')
        self.assertEqual(bus.stops, 'Stop 1, Stop 2, Stop 3')
        self.assertEqual(bus.timings, '10:00, 11:00, 12:00')

    def test_building_creation(self):
        building = Building.objects.create(
            name='Test Building',
            code='TB',
            location='Test Location',
            description='Test Description'
        )
        self.assertEqual(building.name, 'Test Building')
        self.assertEqual(building.code, 'TB')
        self.assertEqual(building.location, 'Test Location')
        self.assertEqual(building.description, 'Test Description')