from django.urls import path
from .views import StageListCreate, StageRetrieveUpdateDestroy

urlpatterns = [
    path('', StageListCreate.as_view(), name='stage-list-create'),
    path('<int:pk>/', StageRetrieveUpdateDestroy.as_view(), name='stage-retrieve-update-destroy'),
]
