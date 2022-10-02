from rest_framework import serializers
from Hvregistration.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'modelnumber', 'vehno', 'ownername', 'aadharnumber', 'mobilenumber', 'email', 'state', 'district', 'tehsil', 'uvp',]

