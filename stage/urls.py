from django.urls import path
from .views import StageListCreate, StageRetrieveUpdateDestroy

urlpatterns = [
    path('stages/', StageListCreate.as_view(), name='stage-list-create'),
    path('stages/<int:pk>/', StageRetrieveUpdateDestroy.as_view(), name='stage-retrieve-update-destroy'),
]
