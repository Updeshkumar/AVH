from rest_framework import serializers
from scregistration.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'contractorname', 'firmname', 'experinceinyear', 'licenseno', 'ulp', 'aadharnumber', 'mobilenumber', 'email', 'state', 'district', 'tehsil', 'uploadworkingimg', 'uploadcontractorphoto',]

