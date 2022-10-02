from django.db import models


class Profile(models.Model):
    labourcontractorname = models.CharField(max_length=200)
    labourwork = models.CharField(max_length=500)
    labourinmembers = models.CharField(max_length=200)
    contractoraadharnumber = models.CharField(max_length=20)
    mobilenumber = models.CharField(max_length=12)    
    email = models.EmailField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    tehsil = models.CharField(max_length=50)
    uploadlobourgroupimg = models.ImageField(upload_to="upimages", blank=True)
    uploadlobourimg = models.ImageField(upload_to="upimages", blank=True)