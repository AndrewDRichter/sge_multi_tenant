from rest_framework.serializers import ModelSerializer
from .models import Entity
from entity_classes.models import EntityClass


class EntitySerializer(ModelSerializer):

    class Meta:
        model = Entity
        fields = '__all__'


class EntityClassSerializer(ModelSerializer):

    class Meta:
        model = EntityClass
        fields = '__all__'


class EntityDetailSerializer(ModelSerializer):
    classes = EntityClassSerializer(many=True)

    class Meta:
        model = Entity
        fields = '__all__'
