# Generated by Django 4.1.2 on 2022-10-23 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_alter_video_audio_file_upload_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_audio_file_upload',
            name='timestamp',
            field=models.DateTimeField(default=datetime.date(2022, 10, 23)),
        ),
    ]
