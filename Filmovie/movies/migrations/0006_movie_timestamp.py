# Generated by Django 3.1.2 on 2021-01-07 19:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20210107_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]