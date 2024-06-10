from .models import *
from rest_framework import serializers

class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = photoUpload
        fields = '__all__'