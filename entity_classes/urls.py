from django.urls import path
from .views import ListEntityClassesAPIView


urlpatterns = [
    path('api/v1/entity_classes/', ListEntityClassesAPIView.as_view(), name='list-entity_classes-api-view'),
]
