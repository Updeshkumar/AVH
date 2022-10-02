from rest_framework import serializers
from registerapi.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'phonenumber', 'password', 'state', "district", "tehsil"]

