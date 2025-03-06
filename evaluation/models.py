from django.db import models
from django.db import models
from utilisateur.models import Utilisateur
class Evaluation(models.Model):
    stagiaire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)  # Relation avec le stagiaire
    date = models.DateField()  # Date de l'évaluation
    note = models.FloatField()  # Note de l'évaluation
    commentaire = models.TextField()  # Commentaire de l'évaluateur

