from django.urls import path
from .views import CandidatureListCreate, CandidatureRetrieveUpdateDestroy

urlpatterns = [
    path('candidatures/', CandidatureListCreate.as_view(), name='candidature-list-create'),
    path('candidatures/<int:pk>/', CandidatureRetrieveUpdateDestroy.as_view(), name='candidature-retrieve-update-destroy'),
]
