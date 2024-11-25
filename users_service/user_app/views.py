from django.shortcuts import render
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import login, logout, authenticate
from .serializers import LoginSerializer, SignUpSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET'])
def root(request, format=None):
    return Response({
        'Login user': request.build_absolute_uri(reverse('login', args=[], kwargs={})),
        'Register user': request.build_absolute_uri(reverse('register', args=[], kwargs={})),
        'Get Token': request.build_absolute_uri(reverse('token_obtain_pair', args=[], kwargs={})),
        'Refresh Token': request.build_absolute_uri(reverse('token_refresh', args=[], kwargs={})),
        'Verify Token': request.build_absolute_uri(reverse('token_verify', args=[], kwargs={})),
        'Test Token': request.build_absolute_uri(reverse('test_token', args=[], kwargs={})),
        
    })

@api_view(['POST'])
def login_user(request):
	serializer = LoginSerializer(data=request.data)
	if serializer.is_valid():
		username = request.data['username']
		password = request.data['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return Response({'Info': 'Login Successful'})
		else:
			return Response({'Info': 'Incorrect username or password'})

	return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])	
def register(request):
	serializer = SignUpSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		response = {
			"info":"Registeration successful",
			"user info":serializer.data
		}
		return Response(data=response, status=status.HTTP_201_CREATED)
	return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_token(request):
	return Response({"info":"JWT auth working"})


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_user_details(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
