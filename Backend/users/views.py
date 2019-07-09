from users.models import *
from users.serializers import *
from rest_framework import generics


class UploadDesign(generics.ListCreateAPIView):
    queryset = Design.objects.all()
    serializer_class =  UploadDesignSerializer

class DesignDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Design.objects.all()
    serializer_class =  UploadDesignSerializer
