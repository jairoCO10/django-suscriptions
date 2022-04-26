from django.shortcuts import render

# Create your views here.
from .models import laboratory
from rest_framework import viewsets
from .serializers import SnippetSerializer
import pandas as pd
import numpy as np

# Create your views here.

class laboratoryViewSet(viewsets.ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = laboratory.objects.all()
    def perform_create(self, serializer):
        serializer.save() 
    def get_queryset(self):
        return self.queryset.filter()
