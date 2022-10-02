from django.contrib import admin
from Hvregistration.models import Profile

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'vehicalname', 'vehno', 'modelnumber', 'ownername', 'aadharnumber', 'mobilenumber', 'email', 'state', 'district', 'tehsil', 'uvp',]

