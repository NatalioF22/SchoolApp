# Generated by Django 4.2.7 on 2024-05-15 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_department_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MajorAttributeRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_count', models.IntegerField(default=1)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.attribute')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.major')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='attributes',
            field=models.ManyToManyField(blank=True, to='courses.attribute'),
        ),
        migrations.AddField(
            model_name='major',
            name='attribute_requirements',
            field=models.ManyToManyField(through='courses.MajorAttributeRequirement', to='courses.attribute'),
        ),
    ]