from rest_framework import generics
from Request.models import  Tailor,User,Request
from Request.serializers import TailorSerializer,UserSerializer,RequestSerializer
# Create your views here.


class RequestList(generics.ListCreateAPIView):

    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Request.objects.all()
        serializer_class = RequestSerializer

