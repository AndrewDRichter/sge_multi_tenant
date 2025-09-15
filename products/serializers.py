from rest_framework import serializers
from products.models import Product
from brands.serializers import BrandSerializer
from categories.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ProductListDetailSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
