from django.urls import path
from django.contrib import admin
from .views import ListCreateUserAPIView, ListCreateEntityAPIView

urlpatterns = [
    path('users/', ListCreateUserAPIView.as_view(), name='list-create-users-api-view'),
    path('entities/', ListCreateEntityAPIView.as_view(), name='list-create-entities-api-view'),
    path('admin/', admin.site.urls),
    # path('', index),
    # path('login', login_view, name='login'),
]
