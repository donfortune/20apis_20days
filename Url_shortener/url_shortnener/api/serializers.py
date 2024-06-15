from .models import *
from rest_framework import serializers

class urlSerializer(serializers.ModelSerializer):
    class Meta:
        model = urlModel
        fields = '__all__'