from django.contrib import admin
from Doregistration.models import Profile

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'drivername', 'vehicalname', 'experinyear', 'mobilenumber', 'aadharnumber', 'alternetmobilenumber', 'licensenumber', 'uploadlicense', 'uploaddriverphoto', 'state', 'district', 'tehsil',]


