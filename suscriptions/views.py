from django.shortcuts import render
from .models import membresia
from rest_framework import viewsets
from .serializers import SnippetSerializer
import pandas as pd
import numpy as np

# Create your views here.

class suscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = membresia.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()
