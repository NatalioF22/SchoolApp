# Generated by Django 4.2.7 on 2024-05-16 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_major_chairman'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='major',
            name='chairman',
        ),
    ]
