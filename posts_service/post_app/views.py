from django.shortcuts import render
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Post
from .serializers import PostSerializer, PostCreateSerializer

# Create your views here.
@api_view(['GET'])
def root(request, format=None):
    return Response({
        'All posts': request.build_absolute_uri(reverse('list_posts', args=[], kwargs={})),
        'Create post': request.build_absolute_uri(reverse('create_post', args=[], kwargs={})),
    })



@api_view(['GET'])
def list_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

"""
@api_view(['GET'])
def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

"""

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    user_id = request.user.id
    serializer = PostCreateSerializer(data=request.data, context={'owner_id': user_id})
    if serializer.is_valid():
        post = serializer.save()
        return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def retrieve_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"message": "Post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist:
        return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)