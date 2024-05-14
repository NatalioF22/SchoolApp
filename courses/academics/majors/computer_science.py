# majors/computer_science.py

from courses.models import Course, Major

def setup_computer_science_major():
    cs_major, created = Major.objects.get_or_create(
        name='Computer Science',
        code='CS',
        description='Computer Science major description',
        minimum_credits=72
    )

    # Add core courses for Computer Science major
    core_courses = [
        'COMP151',  # Computer Science I
        'COMP152',  # Computer Science II
        'COMP206',  # Introduction to Computer Organization
        'COMP250',  # Data Structures and Algorithms
        'COMP340',  # Organization of Programming Languages
        'COMP350',  # Operating Systems
        'COMP430',  # Computer Networks
        'COMP435',  # Analysis of Algorithms
        'COMP390',  # Software Engineering (CWRM)
        'COMP490',  # Senior Design and Development
    ]
    for course_code in core_courses:
        course = Course.objects.get(code=course_code)
        cs_major.core_courses.add(course)

    # Add required courses for Computer Science major
    required_courses = [
        'MATH120',  # Introduction to Linear Algebra
        'MATH130',  # Discrete Mathematics I
        'MATH161',  # Single Variable Calculus I
        'MATH162',  # Single Variable Calculus II
        'MATH200',  # Probability and Statistics
    ]
    for course_code in required_courses:
        course = Course.objects.get(code=course_code)
        cs_major.required_courses.add(course)

    # Add elective courses for Computer Science major
    elective_courses = [
        'COMP3@@',  # Select 5 courses from COMP 3@@ or 4@@
        'COMP4@@',
        'MATH415',
        'PHYS442',
    ]
    for course_code in elective_courses:
        course = Course.objects.get(code=course_code)
        cs_major.elective_courses.add(course)

    # Add natural science requirements for Computer Science major
    natural_science_options = [
        ['BIOL121', 'BIOL122'],  # General Biology I and II
        ['CHEM131', 'CHEM132'],  # Survey of Chemistry I and II
        ['CHEM141', 'CHEM142'],  # Chemical Principles I and II
        ['PHYS181', 'PHYS182'],  # Elements of Physics I and II
        ['PHYS243', 'PHYS244'],  # General Physics I and II
    ]
    for option in natural_science_options:
        courses = Course.objects.filter(code__in=option)
        cs_major.natural_science_courses.add(*courses)

    cs_major.save()