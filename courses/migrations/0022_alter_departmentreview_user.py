# Generated by Django 4.2.7 on 2024-05-16 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_person_profile_pic'),
        ('courses', '0021_alter_departmentcomment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_reviews', to='users.person'),
        ),
    ]