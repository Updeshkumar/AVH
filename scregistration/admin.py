from django.contrib import admin
from scregistration.models import Profile

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'contractorname', 'firmname', 'experinceinyear', 'licenseno', 'ulp', 'aadharnumber', 'mobilenumber', 'email', 'state', 'district', 'tehsil', 'uploadworkingimg', 'uploadcontractorphoto',]
