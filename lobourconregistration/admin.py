from django.contrib import admin
from lobourconregistration.models import Profile

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'labourcontractorname', 'labourwork', 'labourinmembers', 'contractoraadharnumber', 'mobilenumber', 'email', 'state', 'district', 'tehsil', 'uploadlobourgroupimg', 'uploadlobourimg', ]
