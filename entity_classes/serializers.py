from .models import EntityClass
from rest_framework.serializers import ModelSerializer


class EntityClassSerializer(ModelSerializer):

    class Meta:
        model = EntityClass
        fields = '__all__'
