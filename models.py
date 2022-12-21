from django.contrib.auth.models import User
from django.db import models
import os


# Create your models here.
class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pic = models.FileField(upload_to="home/static/home/images/pic")
    color = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def filename(self):
        return os.path.basename(self.pic.name)


class Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    social = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
