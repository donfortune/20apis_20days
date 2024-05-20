from rest_framework import serializers
from .models import User

class apiSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'
        model = User