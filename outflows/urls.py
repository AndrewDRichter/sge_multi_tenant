from django.urls import path
from .views import ListCreateOutflowAPIView, RetrieveUpdateDestroyOutflowAPIView


urlpatterns = [
    path('api/v1/outflows/', ListCreateOutflowAPIView.as_view(), name='list-create-outflow-api-view'),
    path('api/v1/outflows/<int:pk>/', RetrieveUpdateDestroyOutflowAPIView.as_view(), name='retrieve-update-destroy-outflow-api-view'),
]
