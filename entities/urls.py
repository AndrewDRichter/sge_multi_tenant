from django.urls import path
from .views import ListCreateEntityAPIView, RetrieveUpdateDestroyEntityAPIView

urlpatterns = [
    path('api/v1/entities/', ListCreateEntityAPIView.as_view(), name='list-create-entities-api-view'),
    path('api/v1/entities/<int:pk>/', RetrieveUpdateDestroyEntityAPIView.as_view(), name='retrieve-update-destroy-entity-api-view'),
]
