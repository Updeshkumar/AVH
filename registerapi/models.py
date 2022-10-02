from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phonenumber = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    state = models.CharField(max_length=200)
    district = models.CharField(max_length=150)
    tehsil = models.CharField(max_length=230)
