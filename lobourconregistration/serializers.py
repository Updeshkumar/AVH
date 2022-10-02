from rest_framework import serializers
from lobourconregistration.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'labourcontractorname', 'labourwork', 'labourinmembers', 'contractoraadharnumber', 'mobilenumber', 'email', 'state', 'district', 'tehsil', 'uploadlobourgroupimg', 'uploadlobourimg', ]

