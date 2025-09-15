from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/inflows/', views.InflowCreateListAPIView.as_view(), name='inflow-create-list-api-view'),
    path('api/v1/inflows/<int:pk>', views.InflowRetrieveUpdateDestroyAPIView.as_view(), name='inflow-retrieve-update-destroy-api-view'),
]
