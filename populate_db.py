import os
import django

# Set the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # Adjust this to your project settings

# Setup Django
django.setup()

from datetime import date
import random
from faker import Faker
from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from users.models import Person, Student, Professor
from courses.models import Department, Major, Minor, Course

# Initialize Faker
fake = Faker()

# List of US states
us_states = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 
    'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 
    'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
]

departments = [
    {'name': 'Computer Science', 'code': 'CS', 'description': 'Computer Science Department'},
    {'name': 'Mathematics', 'code': 'MATH', 'description': 'Mathematics Department'},
    {'name': 'Physics', 'code': 'PHYS', 'description': 'Physics Department'},
    {'name': 'Chemistry', 'code': 'CHEM', 'description': 'Chemistry Department'},
    {'name': 'Biology', 'code': 'BIOL', 'description': 'Biology Department'},
]

# Create departments if they don't already exist
for dept in departments:
    Department.objects.update_or_create(code=dept['code'], defaults=dept)

# Create majors and minors
majors = [
    {'name': 'Computer Science', 'code': 'CS', 'description': 'Computer Science Major', 'minimum_credits': 120},
    {'name': 'Mathematics', 'code': 'MATH', 'description': 'Mathematics Major', 'minimum_credits': 120},
    {'name': 'Physics', 'code': 'PHYS', 'description': 'Physics Major', 'minimum_credits': 120},
    {'name': 'Chemistry', 'code': 'CHEM', 'description': 'Chemistry Major', 'minimum_credits': 120},
    {'name': 'Biology', 'code': 'BIOL', 'description': 'Biology Major', 'minimum_credits': 120},
]

minors = [
    {'name': 'Computer Science', 'code': 'CS', 'description': 'Computer Science Minor', 'minimum_credits': 18},
    {'name': 'Mathematics', 'code': 'MATH', 'description': 'Mathematics Minor', 'minimum_credits': 18},
    {'name': 'Physics', 'code': 'PHYS', 'description': 'Physics Minor', 'minimum_credits': 18},
    {'name': 'Chemistry', 'code': 'CHEM', 'description': 'Chemistry Minor', 'minimum_credits': 18},
    {'name': 'Biology', 'code': 'BIOL', 'description': 'Biology Minor', 'minimum_credits': 18},
]

for major in majors:
    Major.objects.update_or_create(code=major['code'], defaults=major)

for minor in minors:
    Minor.objects.update_or_create(code=minor['code'], defaults=minor)

# Create courses
courses = [
    {'code': 'CS101', 'name': 'Introduction to Programming', 'description': 'Introductory programming course', 'department': Department.objects.get(code='CS'), 'credits': 3},
    {'code': 'MATH201', 'name': 'Calculus I', 'description': 'Introductory calculus course', 'department': Department.objects.get(code='MATH'), 'credits': 4},
    {'code': 'PHYS101', 'name': 'General Physics I', 'description': 'Introductory physics course', 'department': Department.objects.get(code='PHYS'), 'credits': 4},
    {'code': 'CHEM101', 'name': 'General Chemistry I', 'description': 'Introductory chemistry course', 'department': Department.objects.get(code='CHEM'), 'credits': 4},
    {'code': 'BIOL101', 'name': 'General Biology I', 'description': 'Introductory biology course', 'department': Department.objects.get(code='BIOL'), 'credits': 4},
    {'code': 'CS201', 'name': 'Data Structures and Algorithms', 'description': 'Course on data structures and algorithms', 'department': Department.objects.get(code='CS'), 'credits': 4},
    {'code': 'MATH202', 'name': 'Calculus II', 'description': 'Advanced calculus course', 'department': Department.objects.get(code='MATH'), 'credits': 4},
    {'code': 'PHYS102', 'name': 'General Physics II', 'description': 'Continuation of introductory physics course', 'department': Department.objects.get(code='PHYS'), 'credits': 4},
    {'code': 'CHEM102', 'name': 'General Chemistry II', 'description': 'Continuation of introductory chemistry course', 'department': Department.objects.get(code='CHEM'), 'credits': 4},
    {'code': 'BIOL102', 'name': 'General Biology II', 'description': 'Continuation of introductory biology course', 'department': Department.objects.get(code='BIOL'), 'credits': 4},
    {'code': 'CS301', 'name': 'Operating Systems', 'description': 'Course on operating systems principles', 'department': Department.objects.get(code='CS'), 'credits': 4},
    {'code': 'MATH301', 'name': 'Linear Algebra', 'description': 'Course on linear algebra concepts', 'department': Department.objects.get(code='MATH'), 'credits': 3},
    {'code': 'PHYS301', 'name': 'Modern Physics', 'description': 'Course on modern physics concepts', 'department': Department.objects.get(code='PHYS'), 'credits': 3},
    {'code': 'CHEM301', 'name': 'Organic Chemistry I', 'description': 'Introductory course in organic chemistry', 'department': Department.objects.get(code='CHEM'), 'credits': 4},
    {'code': 'BIOL301', 'name': 'Genetics', 'description': 'Course on genetic principles', 'department': Department.objects.get(code='BIOL'), 'credits': 3},
]

for course in courses:
    Course.objects.update_or_create(code=course['code'], defaults=course)

# Generating dummy data for students
for i in range(100):
    username = f'student{i+1}_{fake.user_name()}'
    password = "password123"  # You can change this to any known password for testing
    user = User.objects.create_user(username=username)
    user.set_password(password)
    user.save()

    first_name = fake.first_name()
    last_name = fake.last_name()
    phone_number = fake.phone_number()
    address = fake.street_address()
    city = fake.city()
    state = random.choice(us_states)
    zip_code = fake.zipcode()
    country = 'USA'
    emergency_contact_name = fake.name()
    emergency_contact_number = fake.phone_number()

    student = Student.objects.create(
        user=user,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        DOB=date(2000, random.randint(1, 12), random.randint(1, 28)),
        race=random.choice(['White', 'Black', 'Asian', 'Hispanic', 'Other']),
        emergency_contact_name=emergency_contact_name,
        emergency_contact_number=emergency_contact_number,
        sex=random.choice(['M', 'F']),
        address=address,
        city=city,
        state=state,
        zip_code=zip_code,
        country=country,
        level=random.choice(['FR', 'SO', 'JR', 'SR', 'GR']),
        class_type=random.choice(['Lecture', 'Lab', 'Seminar']),
        status=random.choice(['FT', 'PT']),
        student_type=random.choice(['D', 'I']),
        campus=random.choice(['Main', 'Satellite']),
        advisor=random.choice(Professor.objects.all()),
        major=random.choice(Major.objects.all()),
        minor=random.choice(Minor.objects.all()),
        gpa=round(random.uniform(2.0, 4.0), 2),
        credits_earned=random.randint(0, 120),
        expected_graduation_date=date(2024, random.randint(1, 12), random.randint(1, 28)),
        is_active=True
    )

    student.classes_taking.set(random.sample(list(Course.objects.all()), 3))
    student.classes_took.set(random.sample(list(Course.objects.all()), 3))
    student.grades = {course.code: random.choice(['A', 'B', 'C', 'D', 'F']) for course in student.classes_took.all()}
    student.save()

# Generating dummy data for professors
for i in range(20):
    username = f'professor{i+1}_{fake.user_name()}'
    password = "password123"  # You can change this to any known password for testing
    user = User.objects.create_user(username=username)
    user.set_password(password)
    user.save()

    first_name = fake.first_name()
    last_name = fake.last_name()
    phone_number = fake.phone_number()
    address = fake.street_address()
    city = fake.city()
    state = random.choice(us_states)
    zip_code = fake.zipcode()
    country = 'USA'
    emergency_contact_name = fake.name()
    emergency_contact_number = fake.phone_number()

    professor = Professor.objects.create(
        user=user,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        DOB=date(1970, random.randint(1, 12), random.randint(1, 28)),
        race=random.choice(['White', 'Black', 'Asian', 'Hispanic', 'Other']),
        emergency_contact_name=emergency_contact_name,
        emergency_contact_number=emergency_contact_number,
        sex=random.choice(['M', 'F']),
        address=address,
        city=city,
        state=state,
        zip_code=zip_code,
        country=country,
        title=random.choice(['ASST', 'ASSOC', 'PROF', 'LECT', 'INST']),
        department=random.choice(Department.objects.all()),
        hire_date=date(2000, random.randint(1, 12), random.randint(1, 28)),
        office_location=f'Building {random.randint(1, 10)} Room {random.randint(100, 500)}',
        office_hours='MWF 9-11am',
        research_interests=fake.text(max_nb_chars=200),
        website=fake.url(),
    )

    professor.courses_teaching.set(random.sample(list(Course.objects.all()), 2))
    professor.save()
