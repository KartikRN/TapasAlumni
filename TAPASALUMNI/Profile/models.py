from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=60)
    tapas_batch = models.IntegerField()
    college = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    main_image = models.ImageField(upload_to='Profile/images',blank = True)
    instagram = models.URLField(max_length=500, default="", blank=True)
    linkedin = models.URLField(max_length=500, default="", blank=True)
    mail = models.URLField(max_length=500, default="", blank=True)
    verified = models.BooleanField(default=False)