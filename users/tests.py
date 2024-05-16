from django.test import TestCase
from django.contrib.auth.models import User
from .models import Person, Student, Professor
from courses.models import Major, Minor, Course, Department
from datetime import date

class PersonModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.person = Person.objects.create(user=self.user, first_name='John', last_name='Doe')

    def test_person_str_representation(self):
        self.assertEqual(str(self.person), 'John Doe')

class StudentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='teststudent')
        self.student = Student.objects.create(user=self.user, first_name='Jane', last_name='Smith', DOB=date(2000, 1, 1))
        self.major = Major.objects.create(name='Computer Science', code='CS')
        self.minor = Minor.objects.create(name='Mathematics', code='MATH')
        self.course1 = Course.objects.create(code='CS101', name='Introduction to Programming', credits=3)
        self.course2 = Course.objects.create(code='CS102', name='Data Structures', credits=4)

    def test_student_get_email(self):
        self.assertEqual(self.student.get_email(), 'J.Smith@student.school.edu')

    def test_student_get_full_name(self):
        self.assertEqual(self.student.get_full_name(), 'Jane Smith')

    def test_student_set_general_info(self):
        advisor = Professor.objects.create(user=User.objects.create(username='testprofessor'), first_name='John', last_name='Doe')
        self.student.set_general_info(level='FR', class_type='Full-time', status='FT', student_type='D', campus='Main Campus', advisor=advisor)
        self.assertEqual(self.student.level, 'FR')
        self.assertEqual(self.student.class_type, 'Full-time')
        self.assertEqual(self.student.status, 'FT')
        self.assertEqual(self.student.student_type, 'D')
        self.assertEqual(self.student.campus, 'Main Campus')
        self.assertEqual(self.student.advisor, advisor)

    def test_student_set_academic_info(self):
        grades = {'CS101': 'A', 'CS102': 'B'}
        self.student.set_academic_info(
            major=self.major,
            minor=self.minor,
            classes_taking=[self.course1],
            classes_took=[self.course2],
            grades=grades,
            gpa=3.5,
            credits_earned=7,
            expected_graduation_date=date(2024, 5, 1)
        )
        self.assertEqual(self.student.major, self.major)
        self.assertEqual(self.student.minor, self.minor)
        self.assertEqual(list(self.student.classes_taking.all()), [self.course1])
        self.assertEqual(list(self.student.classes_took.all()), [self.course2])
        self.assertEqual(self.student.grades, grades)
        self.assertEqual(self.student.gpa, 3.5)
        self.assertEqual(self.student.credits_earned, 7)
        self.assertEqual(self.student.expected_graduation_date, date(2024, 5, 1))

    def test_student_get_age(self):
        current_year = date.today().year
        expected_age = current_year - self.student.DOB.year
        self.assertEqual(self.student.get_age(), expected_age)
    


class ProfessorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testprofessor')
        self.professor = Professor.objects.create(user=self.user, first_name='John', last_name='Doe', title='PROF')
        self.department = Department.objects.create(name='Computer Science', code='CS')
        self.course1 = Course.objects.create(code='CS101', name='Introduction to Programming', credits=3)
        self.course2 = Course.objects.create(code='CS102', name='Data Structures', credits=4)

    def test_professor_get_email(self):
        self.assertEqual(self.professor.get_email(), 'J.Doe@faculty.school.edu')

    def test_professor_get_full_name(self):
        self.assertEqual(self.professor.get_full_name(), 'John Doe')

    def test_professor_courses_teaching(self):
        self.professor.courses_teaching.add(self.course1, self.course2)
        self.assertEqual(list(self.professor.courses_teaching.all()), [self.course1, self.course2])