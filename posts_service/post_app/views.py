from django.shortcuts import render
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET'])
def root(request, format=None):
    return Response({
        'All posts': request.build_absolute_uri(reverse('posts', args=[], kwargs={})),
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def posts(request):
    return Response({"info":"Authorized"})


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