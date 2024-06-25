from . import models
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'

class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCart
        fields = '__all__'  
