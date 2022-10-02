from rest_framework.response import Response
from Hvregistration.models import Profile
from Hvregistration.serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status

class ProfileView(APIView):
    def post(self, request, formate=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'User Register Successfully',
            'status':'success','candidates':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


    def get(self, request, formate=None):
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates, many=True)
        return Response({'status':'success','candidates':serializer.data}, status=status.HTTP_200_OK)






# Create your views here.

