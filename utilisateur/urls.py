from django.urls import path
from .views import UtilisateurListCreate, UtilisateurRetrieveUpdateDestroy

urlpatterns = [
    path('', UtilisateurListCreate.as_view(), name='utilisateur-list-create'),
    path('<int:pk>/', UtilisateurRetrieveUpdateDestroy.as_view(), name='utilisateur-retrieve-update-destroy'),
]
