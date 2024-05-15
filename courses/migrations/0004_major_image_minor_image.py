# Generated by Django 5.0.6 on 2024-05-15 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_department_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='major_images/'),
        ),
        migrations.AddField(
            model_name='minor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='minor_images/'),
        ),
    ]