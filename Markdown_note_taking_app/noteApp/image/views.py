from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
import language_tool_python
# Create your views here.


@api_view(['GET'])
def image_list(request):
    if request.method == 'GET':
        images = photoUpload.objects.all()
        serializer = photoSerializer(images, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def file(request, id):
    if request.method == 'GET':
        image = photoUpload.objects.get(id=id)
        serializer = photoSerializer(image)
        return Response(serializer.data)
    

@api_view(['GET'])
def delete_list(request):
    if request.method == 'GET':
        files = photoUpload.objects.all()
        files.delete()
        return Response("All files deleted")

@api_view(['GET'])
def check_grammar(request, id):
    if request.method == 'GET':
        file = photoUpload.objects.get(id=id)
        file_content = file.file.read().decode('latin-1')
        tool = language_tool_python.LanguageTool('en-US')
        matches = tool.check(file_content)
        return Response(matches)
    

        
