from django.contrib import admin
from registerapi.models import Profile

@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phonenumber', 'password', 'password', 'state', "district", "tehsil", ]


# Register your models here.