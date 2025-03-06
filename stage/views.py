from django.shortcuts import render
from rest_framework import generics
from .models import Stage
from .serializers import StageSerializer

# Create your views here.

# Liste et création des stages
class StageListCreate(generics.ListCreateAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

# Récupération, mise à jour et suppression d'un stage
class StageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
