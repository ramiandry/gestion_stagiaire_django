from rest_framework import serializers
from .models import Candidature

class CandidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidature
        fields = ['id', 'candidat', 'stage', 'dateSoumission', 'statut']
