from rest_framework import serializers
from users.models import *

# آپلود پست
class UploadDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = '__all__'

# sign up
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
