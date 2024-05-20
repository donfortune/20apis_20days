from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from .models import *


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

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = serializers.postSerializer(posts, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def getPost(request, id):
    post = Post.objects.get(id=id)
    serializer = serializers.postSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPost(request):
    data = request.data
    new_post = Post.objects.create(
        title=data['title'],
        content=data['content'],
        #author=data['author']
    )
    serializer = serializers.postSerializer(new_post, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updatePost(request, id):
    data = request.data
    post = Post.objects.get(id=id)
    post.title = data['title']
    post.content = data['content']
    post.save()
    serializer = serializers.postSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deletePost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return Response('Post deleted successfully')