# Generated by Django 4.1.2 on 2022-10-23 14:52

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0007_alter_video_audio_file_upload_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_audio_file_upload',
            name='file_path',
            field=models.FilePathField(default=100, path=pathlib.PureWindowsPath('C:/Users/DELL/OneDrive/Desktop/project/django/DJ')),
            preserve_default=False,
        ),
    ]
