from django.db import models

# Create your models here.

class Stage(models.Model):
    departement = models.CharField(max_length=100)  # Département où se situe le stage
    mission = models.TextField()  # Description de la mission du stage
    duree = models.IntegerField(default=3)  # Durée du stage en mois
    renumeration = models.FloatField(default=0)  # Rémunération du stage
