from django.urls import path
from .views import ListCreateUserAPIView, ListCreateEntityAPIView

urlpatterns = [
    path('users/', ListCreateUserAPIView.as_view(), name='list-create-users-api-view'),
    path('entities/', ListCreateEntityAPIView.as_view(), name='list-create-entities-api-view'),
]
