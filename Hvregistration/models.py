from django.db import models


class Profile(models.Model):
    vehicalname = models.CharField(max_length=200, null=True)
    vehno = models.CharField(max_length=60, blank=True)
    modelnumber = models.CharField(max_length=80)
    ownername = models.CharField(max_length=50)
    aadharnumber = models.CharField(max_length=20)
    mobilenumber = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    tehsil = models.CharField(max_length=50)
    uvp = models.ImageField(upload_to="pimages", blank=True)
   


