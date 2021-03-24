# Generated by Django 3.1.2 on 2021-03-24 16:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_notification_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 3, 24, 16, 26, 46, 750013, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
