from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
import language_tool_python
import markdown
import os
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
    
@api_view(['GET'])
def correct_grammar(request, id):
    if request.method == 'GET':
        file = photoUpload.objects.get(id=id)
        file_content = file.file.read().decode('latin-1')
        tool = language_tool_python.LanguageTool('en-US')
        matches = tool.check(file_content)
        corrected_text = language_tool_python.utils.correct(file_content, matches)
        print(corrected_text)
        return Response({'corrected_text': corrected_text})
    






    
@api_view(['GET'])
def storeMarkdown(request):
    if request.method == 'GET':
        file_path = os.path.join(os.getcwd(), 'files', 'file.md')
        with open(file_path, 'w') as f:
            f.write(file_content)
        # i want to get the corrected file from the check grammar function and then store it in a markdown file
    

        
