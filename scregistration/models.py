from django.db import models


class Profile(models.Model):
    contractorname = models.CharField(max_length=200, null=True)
    firmname = models.CharField(max_length=60, blank=True)
    experinceinyear = models.CharField(max_length=80)
    licenseno = models.CharField(max_length=50)
    ulp = models.ImageField(upload_to="pimages", blank=True)
    aadharnumber = models.CharField(max_length=20)
    mobilenumber = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    tehsil = models.CharField(max_length=50)
    uploadworkingimg = models.ImageField(upload_to="upimages", blank=True)
    uploadcontractorphoto = models.ImageField(upload_to="upimages", blank=True)