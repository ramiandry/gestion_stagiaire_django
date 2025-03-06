from django.shortcuts import render
from rest_framework import generics
from .models import Evaluation
from .serializers import EvaluationSerializer

# Liste et création des évaluations
class EvaluationListCreate(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

# Récupération, mise à jour et suppression d'une évaluation
class EvaluationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

