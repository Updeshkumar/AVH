from rest_framework import serializers
from Doregistration.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'drivername', 'vehicalname', 'experinyear', 'mobilenumber', 'aadharnumber', 'alternetmobilenumber', 'licensenumber', 'uploadlicense', 'uploaddriverphoto', 'state', 'district', 'tehsil',]

