from django.urls import path
from .views import EvaluationListCreate, EvaluationRetrieveUpdateDestroy

urlpatterns = [
    path('evaluations/', EvaluationListCreate.as_view(), name='evaluation-list-create'),
    path('evaluations/<int:pk>/', EvaluationRetrieveUpdateDestroy.as_view(), name='evaluation-retrieve-update-destroy'),
]
