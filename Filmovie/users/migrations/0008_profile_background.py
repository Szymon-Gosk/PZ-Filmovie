# Generated by Django 3.1.2 on 2021-03-06 15:35

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210303_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to=users.models.user_directory_path),
        ),
    ]
