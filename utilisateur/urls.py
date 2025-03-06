from django.urls import path
from .views import UtilisateurListCreate, UtilisateurRetrieveUpdateDestroy

urlpatterns = [
    path('utilisateurs/', UtilisateurListCreate.as_view(), name='utilisateur-list-create'),
    path('utilisateurs/<int:pk>/', UtilisateurRetrieveUpdateDestroy.as_view(), name='utilisateur-retrieve-update-destroy'),
]
