from rest_framework.serializers import ModelSerializer
from products.models import Product
from .models import Outflow


class OutflowSerializer(ModelSerializer):

    class Meta:
        model = Outflow
        fields = '__all__'


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title']


class OutflowDetailSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Outflow
        fields = '__all__'