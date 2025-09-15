from django.urls import path, include

urlpatterns = [
    path('', include('entity_classes.urls')),
]
