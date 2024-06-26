from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<str:pk>/',
        'Create': '/product-create/',
        'Update': '/product-update/<str:pk>/',
        'Delete': '/product-delete/<str:pk>/',
    }
    return (Response(api_urls))

@api_view(['GET'])
def productLists(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productList(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addProduct(request):
    data = {
        'name': request.data['name'],
        'price': request.data['price'],
        'description': request.data['description'],
    }
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateProduct(request, id):
    product = Product.objects.get(id=id)
    data = {
        'name': request.data['name'],
        'price': request.data['price'],
        'description': request.data['description'],
    }
    serializer = ProductSerializer(instance=product, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return Response('Product deleted successfully')


@api_view(['GET'])
def orderItems(request):
    order = OrderItem.objects.all()
    serializer = OrderItemSerializer(order, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def orderItem(request, id):
    order = OrderItem.objects.get(id=id)
    serializer = OrderItemSerializer(order, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createOrderItem(request):
    data = {
        'order': request.data['order'],
        'product': request.data['product'],
        'quantity': request.data['quantity'],
    }
    serializer = OrderItemSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

