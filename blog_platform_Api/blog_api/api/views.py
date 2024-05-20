from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
#from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])

def getRoutes(request):
    routes = [
        {
            'Endpoint': '/api/posts/',
            'method': 'POST',
            'body': None,
            'description': 'Generate JWT Token'},
        {
            'Endpoint': '/api/posts/id/',
            'method': 'POST',
            'body': None,
            'description': 'Refresh'
        },

        {
            'Endpoint': '/api/posts/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Create a new post'
        }
    ]
    return Response(routes)


@api_view(['GET'])
def home(request):
    return Response({'message': 'Hello, World!'})  


@api_view(['GET'])

def protected_view(request):
    return Response({'message': 'This is a protected view, only accessible to authenticated users.'})
