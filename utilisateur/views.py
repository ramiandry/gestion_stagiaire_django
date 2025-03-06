from django.shortcuts import render
from rest_framework import generics
from .models import Utilisateur
from .serializers import UtilisateurSerializer

# Create your views here.

# ListCreateAPIView est une vue générique qui fournit une interface pour lister et créer des objets.
class UtilisateurListCreate(generics.ListCreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

# RetrieveUpdateDestroyAPIView est une vue générique qui fournit une interface pour récupérer, mettre à jour et supprimer un objet.
class UtilisateurRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
