from .models import *
from django import serializers

class photoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoUpload
        fields = '__all__'