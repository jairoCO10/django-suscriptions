from django.shortcuts import render
# Create your views here.
from .models import Sondeo, registroDePerforacion
from rest_framework import viewsets
from .serializers import SnippetSerializer, registroSerializers
import pandas as pd
import numpy as np



class SondeosViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Sondeo.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()

class registroViewSet(viewsets.ModelViewSet):
    serializer_class = registroSerializers
    queryset = registroDePerforacion.objects.all()
    def perform_create(self, serializer):
        serializer.save()
    def get_queryset(self):
        return super().get_queryset()
