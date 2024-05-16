# Generated by Django 4.2.7 on 2024-05-16 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_professor_title'),
        ('courses', '0009_remove_attribute_description_attribute_code_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='chairman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.professor'),
        ),
    ]