from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/products/', views.ProductCreateListAPIView.as_view(), name='product-create-list-api-view'),
    path('api/v1/products/<int:id>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail-api-view'),
]
