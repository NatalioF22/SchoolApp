# Generated by Django 5.0.6 on 2024-05-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_major_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='description',
        ),
        migrations.RemoveField(
            model_name='major',
            name='image',
        ),
        migrations.AddField(
            model_name='department',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='major_images/'),
        ),
    ]
