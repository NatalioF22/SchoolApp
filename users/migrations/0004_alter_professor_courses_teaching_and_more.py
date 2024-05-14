# Generated by Django 5.0.6 on 2024-05-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
        ('users', '0003_alter_person_dob_alter_person_emergency_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='courses_teaching',
            field=models.ManyToManyField(blank=True, null=True, related_name='professors', to='courses.course'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='hire_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='office_hours',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='office_location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='research_interests',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='title',
            field=models.CharField(choices=[('ASST', 'Assistant Professor'), ('ASSOC', 'Associate Professor'), ('PROF', 'Professor'), ('LECT', 'Lecturer'), ('INST', 'Instructor')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
