import os
import django
from django.core.management.base import BaseCommand

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
from courses.models import *



class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    @transaction.atomic
    def handle(self, *args, **options):
        # Initialize Faker
        fake = Faker()
        # List of US states
        us_states = [
            'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 
            'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 
            'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
        ]
        attributes = [
    {'name': 'Global Culture Requirement', 'description': 'Courses that fulfill the global culture requirement'},
    {'name': 'Multiculturalism Requirement', 'description': 'Courses that fulfill the multiculturalism requirement'},
    {'name': 'United States and Massachusetts Constitutions Requirement', 'description': 'Courses that fulfill the US and MA constitutions requirement'},
    {'name': 'Laboratory Science Requirement', 'description': 'Courses that fulfill the laboratory science requirement'},
    {'name': 'Social and Behavioral Sciences Requirement', 'description': 'Courses that fulfill the social and behavioral sciences requirement'},

]
        for attribute in attributes:
            Attribute.objects.get_or_create(name=attribute['name'], defaults=attribute)

        departments = [
            {'name': 'Computer Science', 'code': 'CS', 'description': 'Computer Science Department'},
            {'name': 'Mathematics', 'code': 'MATH', 'description': 'Mathematics Department'},
            {'name': 'Physics', 'code': 'PHYS', 'description': 'Physics Department'},
            {'name': 'Chemistry', 'code': 'CHEM', 'description': 'Chemistry Department'},
            {'name': 'Biology', 'code': 'BIOL', 'description': 'Biology Department'},
            {'name': 'English', 'code': 'ENGL', 'description': 'English Department'},
            {'name': 'History', 'code': 'HIST', 'description': 'History Department'},
            {'name': 'Psychology', 'code': 'PSYC', 'description': 'Psychology Department'},
            {'name': 'Sociology', 'code': 'SOCI', 'description': 'Sociology Department'},
            {'name': 'Economics', 'code': 'ECON', 'description': 'Economics Department'},
            {'name': 'Political Science', 'code': 'POLS', 'description': 'Political Science Department'},
            {'name': 'Art', 'code': 'ART', 'description': 'Art Department'},
            {'name': 'Music', 'code': 'MUSC', 'description': 'Music Department'},
            {'name': 'Theatre', 'code': 'THEA', 'description': 'Theatre Department'},
            {'name': 'Philosophy', 'code': 'PHIL', 'description': 'Philosophy Department'},
            {'name': 'Anthropology', 'code': 'ANTH', 'description': 'Anthropology Department'},
            {'name': 'Geography', 'code': 'GEOG', 'description': 'Geography Department'},
            {'name': 'Linguistics', 'code': 'LING', 'description': 'Linguistics Department'},
            {'name': 'Religion', 'code': 'RELI', 'description': 'Religion Department'},
            {'name': 'Classics', 'code': 'CLAS', 'description': 'Classics Department'},
        ]

        # Create departments if they don't already exist
        for dept in departments:
            Department.objects.get_or_create(code=dept['code'], defaults=dept)

        # Create majors and minors
        majors = [
            {'name': 'Computer Science', 'code': 'CS', 'description': 'Computer Science Major', 'minimum_credits': 120},
            {'name': 'Mathematics', 'code': 'MATH', 'description': 'Mathematics Major', 'minimum_credits': 120},
            {'name': 'Physics', 'code': 'PHYS', 'description': 'Physics Major', 'minimum_credits': 120},
            {'name': 'Chemistry', 'code': 'CHEM', 'description': 'Chemistry Major', 'minimum_credits': 120},
            {'name': 'Biology', 'code': 'BIOL', 'description': 'Biology Major', 'minimum_credits': 120},
            {'name': 'English', 'code': 'ENGL', 'description': 'English Major', 'minimum_credits': 120},
            {'name': 'History', 'code': 'HIST', 'description': 'History Major', 'minimum_credits': 120},
            {'name': 'Psychology', 'code': 'PSYC', 'description': 'Psychology Major', 'minimum_credits': 120},
            {'name': 'Sociology', 'code': 'SOCI', 'description': 'Sociology Major', 'minimum_credits': 120},
            {'name': 'Economics', 'code': 'ECON', 'description': 'Economics Major', 'minimum_credits': 120},
            {'name': 'Political Science', 'code': 'POLS', 'description': 'Political Science Major', 'minimum_credits': 120},
            {'name': 'Art', 'code': 'ART', 'description': 'Art Major', 'minimum_credits': 120},
            {'name': 'Music', 'code': 'MUSC', 'description': 'Music Major', 'minimum_credits': 120},
            {'name': 'Theatre', 'code': 'THEA', 'description': 'Theatre Major', 'minimum_credits': 120},
            {'name': 'Philosophy', 'code': 'PHIL', 'description': 'Philosophy Major', 'minimum_credits': 120},
            {'name': 'Anthropology', 'code': 'ANTH', 'description': 'Anthropology Major', 'minimum_credits': 120},
            {'name': 'Geography', 'code': 'GEOG', 'description': 'Geography Major', 'minimum_credits': 120},
            {'name': 'Linguistics', 'code': 'LING', 'description': 'Linguistics Major', 'minimum_credits': 120},
            {'name': 'Religion', 'code': 'RELI', 'description': 'Religion Major', 'minimum_credits': 120},
            {'name': 'Classics', 'code': 'CLAS', 'description': 'Classics Major', 'minimum_credits': 120},
        ]

        minors = [
            {'name': 'Computer Science', 'code': 'CS', 'description': 'Computer Science Minor', 'minimum_credits': 18},
            {'name': 'Mathematics', 'code': 'MATH', 'description': 'Mathematics Minor', 'minimum_credits': 18},
            {'name': 'Physics', 'code': 'PHYS', 'description': 'Physics Minor', 'minimum_credits': 18},
            {'name': 'Chemistry', 'code': 'CHEM', 'description': 'Chemistry Minor', 'minimum_credits': 18},
            {'name': 'Biology', 'code': 'BIOL', 'description': 'Biology Minor', 'minimum_credits': 18},
            {'name': 'English', 'code': 'ENGL', 'description': 'English Minor', 'minimum_credits': 18},
            {'name': 'History', 'code': 'HIST', 'description': 'History Minor', 'minimum_credits': 18},
            {'name': 'Psychology', 'code': 'PSYC', 'description': 'Psychology Minor', 'minimum_credits': 18},
            {'name': 'Sociology', 'code': 'SOCI', 'description': 'Sociology Minor', 'minimum_credits': 18},
            {'name': 'Economics', 'code': 'ECON', 'description': 'Economics Minor', 'minimum_credits': 18},
            {'name': 'Political Science', 'code': 'POLS', 'description': 'Political Science Minor', 'minimum_credits': 18},
            {'name': 'Art', 'code': 'ART', 'description': 'Art Minor', 'minimum_credits': 18},
            {'name': 'Music', 'code': 'MUSC', 'description': 'Music Minor', 'minimum_credits': 18},
            {'name': 'Theatre', 'code': 'THEA', 'description': 'Theatre Minor', 'minimum_credits': 18},
            {'name': 'Philosophy', 'code': 'PHIL', 'description': 'Philosophy Minor', 'minimum_credits': 18},
            {'name': 'Anthropology', 'code': 'ANTH', 'description': 'Anthropology Minor', 'minimum_credits': 18},
            {'name': 'Geography', 'code': 'GEOG', 'description': 'Geography Minor', 'minimum_credits': 18},
            {'name': 'Linguistics', 'code': 'LING', 'description': 'Linguistics Minor', 'minimum_credits': 18},
            {'name': 'Religion', 'code': 'RELI', 'description': 'Religion Minor', 'minimum_credits': 18},
            {'name': 'Classics', 'code': 'CLAS', 'description': 'Classics Minor', 'minimum_credits': 18},
        ]

        for major in majors:
            Major.objects.get_or_create(code=major['code'], defaults=major)

        for minor in minors:
            Minor.objects.get_or_create(code=minor['code'], defaults=minor)

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
            {'code': 'CS401', 'name': 'Machine Learning', 'description': 'Introduction to machine learning concepts', 'department': Department.objects.get(code='CS'), 'credits': 4},
            {'code': 'MATH401', 'name': 'Abstract Algebra', 'description': 'Course on abstract algebra concepts', 'department': Department.objects.get(code='MATH'), 'credits': 3},
            {'code': 'PHYS401', 'name': 'Quantum Mechanics', 'description': 'Course on quantum mechanics principles', 'department': Department.objects.get(code='PHYS'), 'credits': 3},
            {'code': 'CHEM401', 'name': 'Biochemistry', 'description': 'Course on biochemical principles', 'department': Department.objects.get(code='CHEM'), 'credits': 4},
            {'code': 'BIOL401', 'name': 'Microbiology', 'description': 'Course on microbiology principles', 'department': Department.objects.get(code='BIOL'), 'credits': 4},
            {'code': 'CS102', 'name': 'Introduction to Computer Science', 'description': 'Basic concepts in computer science', 'department': Department.objects.get(code='CS'), 'credits': 3},
            {'code': 'MATH102', 'name': 'Discrete Mathematics', 'description': 'Course on discrete mathematics concepts', 'department': Department.objects.get(code='MATH'), 'credits': 3},
            {'code': 'PHYS102', 'name': 'Thermodynamics', 'description': 'Introduction to thermodynamics', 'department': Department.objects.get(code='PHYS'), 'credits': 3},
            {'code': 'CHEM102', 'name': 'Inorganic Chemistry', 'description': 'Course on inorganic chemistry principles', 'department': Department.objects.get(code='CHEM'), 'credits': 3},
            {'code': 'BIOL102', 'name': 'Anatomy and Physiology', 'description': 'Course on human anatomy and physiology', 'department': Department.objects.get(code='BIOL'), 'credits': 4},
            {'code': 'CS202', 'name': 'Software Engineering', 'description': 'Introduction to software engineering principles', 'department': Department.objects.get(code='CS'), 'credits': 4},
            {'code': 'MATH202', 'name': 'Probability and Statistics', 'description': 'Course on probability and statistics', 'department': Department.objects.get(code='MATH'), 'credits': 3},
            {'code': 'PHYS202', 'name': 'Electromagnetism', 'description': 'Course on electromagnetism principles', 'department': Department.objects.get(code='PHYS'), 'credits': 4},
            {'code': 'CHEM202', 'name': 'Analytical Chemistry', 'description': 'Course on analytical chemistry techniques', 'department': Department.objects.get(code='CHEM'), 'credits': 3},
            {'code': 'BIOL202', 'name': 'Cell Biology', 'description': 'Course on cellular biology principles', 'department': Department.objects.get(code='BIOL'), 'credits': 4},
            {'code': 'CS302', 'name': 'Computer Networks', 'description': 'Course on computer networking principles', 'department': Department.objects.get(code='CS'), 'credits': 4},
            {'code': 'MATH302', 'name': 'Differential Equations', 'description': 'Course on differential equations', 'department': Department.objects.get(code='MATH'), 'credits': 3},
            {'code': 'PHYS302', 'name': 'Optics', 'description': 'Introduction to optics principles', 'department': Department.objects.get(code='PHYS'), 'credits': 3},
            {'code': 'CHEM302', 'name': 'Physical Chemistry', 'description': 'Course on physical chemistry principles', 'department': Department.objects.get(code='CHEM'), 'credits': 4},
            {'code': 'BIOL302', 'name': 'Ecology', 'description': 'Course on ecological principles', 'department': Department.objects.get(code='BIOL'), 'credits': 4},
            {'code': 'CS402', 'name': 'Artificial Intelligence', 'description': 'Course on artificial intelligence concepts', 'department': Department.objects.get(code='CS'), 'credits': 4},
            {'code': 'MATH402', 'name': 'Number Theory', 'description': 'Course on number theory concepts', 'department': Department.objects.get(code='MATH'), 'credits': 3},
            {'code': 'PHYS402', 'name': 'Nuclear Physics', 'description': 'Course on nuclear physics principles', 'department': Department.objects.get(code='PHYS'), 'credits': 3},
            {'code': 'CHEM402', 'name': 'Environmental Chemistry', 'description': 'Course on environmental chemistry', 'department': Department.objects.get(code='CHEM'), 'credits': 4},
            {'code': 'BIOL402', 'name': 'Evolutionary Biology', 'description': 'Course on evolutionary biology', 'department': Department.objects.get(code='BIOL'), 'credits': 3},
            {'code': 'CS103', 'name': 'Web Development', 'description': 'Introduction to web development', 'department': Department.objects.get(code='CS'), 'credits': 3},
            {'code': 'MATH103', 'name': 'Geometry', 'description': 'Course on geometry principles', 'department': Department.objects.get(code='MATH'), 'credits': 3},
            {'code': 'PHYS103', 'name': 'Classical Mechanics', 'description': 'Course on classical mechanics principles', 'department': Department.objects.get(code='PHYS'), 'credits': 4},
            {'code': 'CHEM103', 'name': 'Polymer Chemistry', 'description': 'Introduction to polymer chemistry', 'department': Department.objects.get(code='CHEM'), 'credits': 3},
            {'code': 'BIOL103', 'name': 'Plant Biology', 'description': 'Course on plant biology principles', 'department': Department.objects.get(code='BIOL'), 'credits': 4},
            {'code': 'CS203', 'name': 'Database Systems', 'description': 'Course on database systems', 'department': Department.objects.get(code='CS'), 'credits': 4},
            {'code': 'MATH203', 'name': 'Complex Variables', 'description': 'Course on complex variables', 'department': Department.objects.get(code='MATH'), 'credits': 3},
            {'code':

        'PHYS203', 'name': 'Astrophysics', 'description': 'Introduction to astrophysics', 'department': Department.objects.get(code='PHYS'), 'credits': 3},
            {'code': 'CHEM203', 'name': 'Medicinal Chemistry', 'description': 'Course on medicinal chemistry principles', 'department': Department.objects.get(code='CHEM'), 'credits': 3},
            {'code': 'BIOL203', 'name': 'Neuroscience', 'description': 'Course on neuroscience principles', 'department': Department.objects.get(code='BIOL'), 'credits': 4},
        ]
        for course in courses:
            Course.objects.get_or_create(code=course['code'], defaults=course)

       

        # Generating dummy data for professors
        for i in range(20):
            username = f'professor{i+1}_{fake.user_name()}'
            password = "password123"  # You can change this to any known password for testing
            
            if User.objects.filter(username=username).exists():
                continue
            
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
         # Generating dummy data for students
        for i in range(100):
            username = f'student{i+1}_{fake.user_name()}'
            password = "password123"  # You can change this to any known password for testing
            
            if User.objects.filter(username=username).exists():
                continue
            
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