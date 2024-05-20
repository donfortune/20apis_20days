from rest_framework import serializers
from .models import User, Post

class apiSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class postSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Post