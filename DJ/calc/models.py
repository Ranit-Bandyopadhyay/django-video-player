from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
import os
from django.conf import settings
Base=settings.BASE_DIR
cc=os.path.join(Base,'media')

# Create your models here.
class video_audio_file_upload(models.Model):
    ids=models.AutoField(primary_key=True)
    file_name=models.CharField(max_length=255)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    my_file=models.FileField(upload_to='')

    def __str__(self) -> str:
        return self.file_name
        

'----------------------------------------------------------------------------------------------'
class document_file_upload(models.Model):
    idsd=models.AutoField(primary_key=True)
    file_named=models.CharField(max_length=255)
    timestampd=models.DateTimeField(auto_now=False,auto_now_add=True)
    my_filed=models.FileField(upload_to='')

    def __str__(self) -> str:
        return self.file_named
'--------------------------------------------------------------------------------------------'