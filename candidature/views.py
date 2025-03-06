from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Candidature
from .serializers import CandidatureSerializer

# Liste et création des candidatures
class CandidatureListCreate(generics.ListCreateAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer

# Récupération, mise à jour et suppression d'une candidature
class CandidatureRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
