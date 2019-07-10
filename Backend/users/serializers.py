from rest_framework import serializers
from users.models import *

# Log in
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# آپلود پست
class UploadDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = '__all__'

