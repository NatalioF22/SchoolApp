from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from WebApp.models import Professor, Student, Subject
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **options):
        fake = Faker()
        User = get_user_model()

        # Create admin user
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(username='admin', email='admin@example.com', password='admin123')

        # Define subject names and codes
        subjects = [
            ('Mathematics', 'MATH'), ('Computer Science', 'CSCI'), ('English Literature', 'ENGL'),
            ('Physics', 'PHYS'), ('Chemistry', 'CHEM'), ('Biology', 'BIOL'), ('History', 'HIST'),
            ('Geography', 'GEOG'), ('Psychology', 'PSYC'), ('Economics', 'ECON'),
            ('Business Administration', 'BADM'), ('Art History', 'ARTH'), ('Music Theory', 'MUTH'),
            ('Political Science', 'POLS'), ('Sociology', 'SOCI')
        ]

        # Create professors
        professors = []
        for _ in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f"{first_name.lower()}.{last_name.lower()}"
            password = fake.password()
            professor = Professor.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone_number=fake.phone_number(),
                DOB=fake.date_of_birth(minimum_age=30, maximum_age=65),
                race=fake.random_element(elements=('White', 'Black', 'Asian', 'Hispanic', 'Other')),
                emergency_contact_name=fake.name(),
                emergency_contact_number=fake.phone_number(),
                sex=fake.random_element(elements=('M', 'F')),
                status=fake.random_element(elements=('FT', 'PT')),
                professor_type=fake.random_element(elements=('Adjunct', 'Assistant', 'Associate', 'Full'))
            )
            professor.setAdacemicInfo(classes_taught=[])
            User.objects.create_user(username=username, password=password)
            professors.append((username, password, professor))

        # Create students
        students = []
        for _ in range(50):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f"{first_name.lower()}.{last_name.lower()}"
            password = fake.password()
            student = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone_number=fake.phone_number(),
                DOB=fake.date_of_birth(minimum_age=18, maximum_age=25),
                race=fake.random_element(elements=('White', 'Black', 'Asian', 'Hispanic', 'Other')),
                emergency_contact_name=fake.name(),
                emergency_contact_number=fake.phone_number(),
                sex=fake.random_element(elements=('M', 'F'))
            )
            student.setGeneralInfo(
                level=fake.random_element(elements=('Freshman', 'Sophomore', 'Junior', 'Senior')),
                class_type=fake.random_element(elements=('Full-time', 'Part-time')),
                status=fake.random_element(elements=('Active', 'Inactive')),
                student_type=fake.random_element(elements=('Domestic', 'International')),
                campus=fake.city(),
                advisor=Professor.objects.order_by('?').first()
            )
            student.setAdacemicInfo(classes_taking=[], classes_took=[], grades=[])
            User.objects.create_user(username=username, password=password)
            students.append((username, password, student))

        # Create subjects
        for subject_name, subject_code in subjects:
            for level in range(100, 500, 100):
                Subject.objects.create(
                    CRN=str(fake.random_number(digits=6)),
                    title=f"{subject_name} {level}",
                    code=f"{subject_code}-{level}",
                    section=fake.random_element(elements=('001', '002', '003')),
                    credits=fake.random_element(elements=(3, 4)),
                    prerequisites=[],
                    meeting_times=[],
                    attributes={},
                    professor=Professor.objects.order_by('?').first()
                )

        # Assign students to subjects
        for _, _, student in students:
            total_credits = 0
            while total_credits < 18:
                subject = Subject.objects.order_by('?').first()
                if subject not in student.classes_enrolled.all():
                    student.classes_enrolled.add(subject)
                    total_credits += subject.credits

        # Generate CSS file with usernames and passwords
        css_content = ""
        for username, password, _ in professors:
            css_content += f".professor-{username}::before {{content: 'Username: {username}, Password: {password}'}}\n"
        for username, password, _ in students:
            css_content += f".student-{username}::before {{content: 'Username: {username}, Password: {password}'}}\n"

        with open('usernames.css', 'w') as file:
            file.write(css_content)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data.'))