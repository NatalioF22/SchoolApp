# Generated by Django 5.0.6 on 2024-05-16 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_departmentcomment'),
        ('users', '0009_person_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseoutline',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_outlines', to='users.person'),
        ),
    ]
