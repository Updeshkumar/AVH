from django.db import models


class Profile(models.Model):
    vehicalname = models.CharField(max_length=50)
    experinyear = models.CharField(max_length=200)
    drivername = models.CharField(max_length=150)
    aadharnumber = models.CharField(max_length=20)
    mobilenumber = models.CharField(max_length=12)
    alternetmobilenumber = models.CharField(max_length=12)
    licensenumber = models.CharField(max_length=200)
    uploadlicense = models.ImageField(upload_to="pimages", blank=True)
    uploaddriverphoto = models.ImageField(upload_to="pimages", blank=True)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    tehsil = models.CharField(max_length=50)
 

