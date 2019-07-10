from users.models import *
from users.serializers import *
from rest_framework import generics

class CreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

class UploadDesign(generics.ListCreateAPIView):
    queryset = Design.objects.all()
    serializer_class =  UploadDesignSerializer

class DesignDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Design.objects.all()
    serializer_class =  UploadDesignSerializer
