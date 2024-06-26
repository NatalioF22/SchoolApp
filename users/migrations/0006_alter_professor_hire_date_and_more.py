# Generated by Django 5.0.6 on 2024-05-13 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_person_dob_alter_person_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='hire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='office_hours',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='office_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='research_interests',
            field=models.TextField(blank=True, null=True),
        ),
    ]
