from django.db import models

# Create your models here.


class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Email unique pour chaque utilisateur
    mot_de_Passe = models.CharField(max_length=100)  # Vous pourriez utiliser Django User pour gérer les mots de passe
    role = models.CharField(max_length=50)  # Role de l'utilisateur (admin, user, etc.)
