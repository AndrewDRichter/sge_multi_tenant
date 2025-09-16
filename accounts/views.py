from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser


class ListCreateUserAPIView(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
