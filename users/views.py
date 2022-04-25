from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core import serializers
from django.http import JsonResponse, HttpResponse, response
from rest_framework import status, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from django.forms.models import model_to_dict

from .serializers import UserSerializer
from .models import User


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])

def current_user(request):
    serializer = UserSerializer(request.User)
    return Response(serializer.data)


class UserList(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        #Token.objects.get_or_create(user=request.user)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def login(request):
    token, created = Token.objects.get_or_create(user=request.user)
    return JsonResponse({
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "token": token.key
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_information(request):
    userData = model_to_dict(request.user)    
    del userData['password']
    return JsonResponse({
        "email": request.user.email,
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,    
    })
