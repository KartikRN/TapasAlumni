from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextUploadingField()
    date = models.DateField()