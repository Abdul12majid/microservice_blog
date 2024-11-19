from django.shortcuts import render
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def root(request, format=None):
    return Response({
        'All': "no urls yet",
        
    })