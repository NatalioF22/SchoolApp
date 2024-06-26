# Generated by Django 5.0.6 on 2024-05-13 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('DOB', models.DateField()),
                ('race', models.CharField(max_length=50)),
                ('emergency_contact_name', models.CharField(max_length=50)),
                ('emergency_contact_number', models.CharField(max_length=20)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.person')),
                ('title', models.CharField(choices=[('ASST', 'Assistant Professor'), ('ASSOC', 'Associate Professor'), ('PROF', 'Professor'), ('LECT', 'Lecturer'), ('INST', 'Instructor')], max_length=5)),
                ('hire_date', models.DateField()),
                ('office_location', models.CharField(max_length=100)),
                ('office_hours', models.TextField()),
                ('research_interests', models.TextField()),
                ('website', models.URLField(blank=True)),
                ('courses_teaching', models.ManyToManyField(blank=True, related_name='professors', to='courses.course')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.department')),
            ],
            bases=('users.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.person')),
                ('level', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=2)),
                ('class_type', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time')], max_length=2)),
                ('student_type', models.CharField(choices=[('D', 'Domestic'), ('I', 'International')], max_length=1)),
                ('campus', models.CharField(max_length=100)),
                ('grades', models.JSONField(blank=True, default=dict)),
                ('gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('credits_earned', models.IntegerField(default=0)),
                ('expected_graduation_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('advisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advised_students', to='users.professor')),
                ('classes_taking', models.ManyToManyField(blank=True, related_name='students_enrolled', to='courses.course')),
                ('classes_took', models.ManyToManyField(blank=True, related_name='students_completed', to='courses.course')),
                ('major', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.major')),
                ('minor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.minor')),
            ],
            bases=('users.person',),
        ),
    ]
