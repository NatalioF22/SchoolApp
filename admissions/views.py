from django.test import TestCase
from django.contrib.auth.models import User
from courses.models import Major

from admissions.models import *

class ApplicationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.major = Major.objects.create(name='Computer Science')

    def test_application_creation(self):
        application = Application.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            major=self.major
        )

        self.assertEqual(application.user, self.user)
        self.assertEqual(application.first_name, 'John')
        self.assertEqual(application.last_name, 'Doe')
        self.assertEqual(application.email, 'john@example.com')
        self.assertEqual(application.major, self.major)
        self.assertEqual(application.status, 'pending')

    def test_application_str_representation(self):
        application = Application.objects.create(
            user=self.user,
            first_name='Jane',
            last_name='Smith',
            email='jane@example.com',
            status='accepted'
        )

        expected_str = 'Jane Smith - accepted'
        self.assertEqual(str(application), expected_str)

    def test_application_status_choices(self):
        status_choices = Application.STATUS_CHOICES

        self.assertIn(('pending', 'Pending'), status_choices)
        self.assertIn(('accepted', 'Accepted'), status_choices)
        self.assertIn(('rejected', 'Rejected'), status_choices)