# Generated by Django 5.0.6 on 2024-05-16 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_blog', '0001_initial'),
        ('users', '0009_person_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='date_published',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='approved',
            new_name='is_approved',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='school_blog.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.person'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='school_blog.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.person'),
        ),
    ]
