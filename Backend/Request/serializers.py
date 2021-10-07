from rest_framework import serializers
from django.contrib.auth.models import User
from Request.models import Tailor,User,Request


class RequestSerializer(serializers.ModelSerializer):
        class Meta:
            model = Request
            fields = '__all__'


class TailorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Tailor
            fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
