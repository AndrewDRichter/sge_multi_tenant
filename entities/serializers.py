from rest_framework.serializers import ModelSerializer
from .models import Entity
from django.contrib.auth import get_user_model


class EntitySerializer(ModelSerializer):

    class Meta:
        model = Entity
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = '__all__'
