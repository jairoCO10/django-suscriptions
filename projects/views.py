from itertools import count
from django.shortcuts import render

# Create your views here.
from turtle import home
from django.http import JsonResponse, HttpResponse
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from rest_framework.parsers import JSONParser
from .models import home1
from .serializers import SnippetSerializer
from rest_framework import viewsets
import pandas as pd


class homeViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = home1.objects.all()
    dato = pd.DataFrame(home1.objects.all())
    user_Count = home1.objects.all().count()
    count = 5
    if (user_Count <= count):
        print(user_Count)
        def perform_create(self, serializer):
            counts = home1.cantidad
            datos = pd.DataFrame(home1.objects.all()).count()
            if (home1.cantidad == counts):
                serializer.save(iduser=self.request.user) 
        def get_queryset(self):
            return self.queryset.filter(iduser=self.request.user)
    else :
        print("usted no puede agregar mas datos")


@api_view(['PUT','POST', 'GET'])
def home_post_CRUD(request, id=0):
    if request.method == "PUT":
        if id==0:
            upddato = home1.objects.get(pk=id)
            form = serialize(instance=upddato)
            return JsonResponse(form)
    if request.method == 'POST':
        datos =json.loads(request.body)
        newproject = home1(**datos)
        newproject.save()
        dato= model_to_dict(newproject)
        return JsonResponse(dato)
    

@api_view(['GET'])
def home_get_CRUD(request):
    if request.method == 'GET':
        dato = pd.DataFrame(home1.objects.all().values())
        return JsonResponse(dato.to_dict('records'), safe=False)

@csrf_exempt
def home_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = home1.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def home_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = home1.objects.get(pk=pk)
    except home1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
