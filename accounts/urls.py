from django.urls import path
from accounts.jwt import TenantTokenObtainPairView
from accounts.views import ListCreateUserAPIView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('api/v1/accounts/', ListCreateUserAPIView.as_view(), name='list-create-users-api-view'),
    path('api/v1/accounts/token/', TenantTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/accounts/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

