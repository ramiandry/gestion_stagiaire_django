from django.db import models
from utilisateur.models import Utilisateur  
from stage.models import Stage

class Candidature(models.Model):
    candidat = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)  # Relation avec le modèle Stagiaire
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)  # Relation avec le modèle Stage
    dateSoumission = models.DateField()  # La date de soumission de la candidature
    statut = models.CharField(max_length=50)  # Le statut de la candidature (ex : "En cours", "Acceptée", "Rejetée")

