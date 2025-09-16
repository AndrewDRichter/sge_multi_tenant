from rest_framework.serializers import ModelSerializer
from inflows.models import Inflow
from entities.models import Entity
from products.models import Product


class InflowSerializer(ModelSerializer):

    class Meta:
        model = Inflow
        fields = '__all__'


class EntitySerializer(ModelSerializer):

    class Meta:
        model = Entity
        fields = ['id', 'name']


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title']


class InflowDetailSerializer(ModelSerializer):
    supplier = EntitySerializer()
    product = ProductSerializer()

    class Meta:
        model = Inflow
        fields = '__all__'
