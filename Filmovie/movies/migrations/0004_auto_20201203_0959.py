# Generated by Django 3.1.2 on 2020-12-03 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='like',
            new_name='like_type',
        ),
    ]