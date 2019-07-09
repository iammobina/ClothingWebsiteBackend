from rest_framework import serializers
from users.models import *

# آپلود پست
class UploadDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = '__all__'
