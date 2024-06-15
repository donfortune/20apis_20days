from django.shortcuts import render, redirect
from .forms import URLForm
from .models import urlModel
from .utils import generate_short_url
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import urlSerializer
import random, string


def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@api_view(['GET'])
def listUrls(request):
    urls = urlModel.objects.all()
    serializer = urlSerializer(urls, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUrl(request):
    data = request.data
    url = urlModel.objects.create(original_url=request.data['original_url'], short_url=request.data['short_url'])
    serializer = urlSerializer(url, many=False)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def generateShortUrl(request, id):
    url = urlModel.objects.get(id=id)
    print(url)
    url.short_url = generate_short_url()
    print(url.short_url)
    url.save()
    serializer = urlSerializer(url, many=False)
    return Response(serializer.data)


