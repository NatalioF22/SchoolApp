from django.test import TestCase
from django.core.exceptions import ValidationError
from courses.models import *
from users.models import *

class DepartmentModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name='Computer Science', code='CS')

    def test_department_str_representation(self):
        self.assertEqual(str(self.department), 'Computer Science')

    def test_department_get_courses(self):
        course1 = Course.objects.create(name='Programming 101', code='CS101', department=self.department, credits=3)
        course2 = Course.objects.create(name='Data Structures', code='CS201', department=self.department, credits=4)
        courses = self.department.get_courses()
        self.assertEqual(list(courses), [course1, course2])

    def test_department_get_majors(self):
        major = Major.objects.create(name='Computer Science', code='CS', department=self.department)
        course = Course.objects.create(name='Programming 101', code='CS101', department=self.department, credits=3)
        major.core_courses.add(course)
        majors = self.department.get_majors()
        self.assertEqual(list(majors), [major])

    def test_department_clean_chairperson_validation(self):
        # Test case where the chairperson does not have the title 'CHAIR'
        with self.assertRaises(ValidationError):
            professor = Professor.objects.create(first_name='John', last_name='Doe', title='PROFESSOR')
            self.department.chairperson = professor
            self.department.clean()

class CourseModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name='Computer Science', code='CS')
        self.course = Course.objects.create(name='Programming 101', code='CS101', department=self.department, credits=3)

    def test_course_str_representation(self):
        self.assertEqual(str(self.course), 'CS101 - Programming 101')

    def test_course_generate_unique_code(self):
        code = Course.generate_unique_code()
        self.assertIsInstance(code, str)
        self.assertEqual(len(code), 6)

class MajorModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name='Computer Science', code='CS')
        self.major = Major.objects.create(name='Computer Science', code='CS', department=self.department)
        self.course1 = Course.objects.create(name='Programming 101', code='CS101', department=self.department, credits=3)
        self.course2 = Course.objects.create(name='Data Structures', code='CS201', department=self.department, credits=4)

    def test_major_str_representation(self):
        self.assertEqual(str(self.major), 'Computer Science')

    def test_major_get_total_credits(self):
        self.major.core_courses.add(self.course1)
        self.major.required_courses.add(self.course2)
        total_credits = self.major.get_total_credits()
        self.assertEqual(total_credits, 7)

    def test_major_is_requirements_met(self):
        student = Student.objects.create(first_name='John', last_name='Doe')
        student.classes_took.add(self.course1)
        self.major.core_courses.add(self.course1)
        self.major.required_courses.add(self.course2)
        self.assertFalse(self.major.is_requirements_met(student))
        student.classes_took.add(self.course2)
        self.assertTrue(self.major.is_requirements_met(student))

    def test_major_clean_attribute_requirements_validation(self):
        attribute = Attribute.objects.create(name='Math')
        major_attribute_requirement = MajorAttributeRequirement.objects.create(major=self.major, attribute=attribute, required_count=1)
        with self.assertRaises(ValidationError):
            self.major.clean()

class MinorModelTest(TestCase):
    def setUp(self):
        self.minor = Minor.objects.create(name='Data Science', code='DS')
        self.course1 = Course.objects.create(name='Introduction to Data Science', code='DS101', credits=3)
        self.course2 = Course.objects.create(name='Machine Learning', code='DS201', credits=4)

    def test_minor_str_representation(self):
        self.assertEqual(str(self.minor), 'Data Science')

    def test_minor_get_total_credits(self):
        self.minor.required_courses.add(self.course1)
        self.minor.required_courses.add(self.course2)
        total_credits = self.minor.get_total_credits()
        self.assertEqual(total_credits, 7)

    def test_minor_is_requirements_met(self):
        student = Student.objects.create(first_name='John', last_name='Doe')
        student.classes_took.add(self.course1)
        self.minor.required_courses.add(self.course1)
        self.minor.required_courses.add(self.course2)
        self.assertFalse(self.minor.is_requirements_met(student))
        student.classes_took.add(self.course2)
        self.assertTrue(self.minor.is_requirements_met(student))