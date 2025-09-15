from rest_framework import generics
from products.serializers import ProductSerializer, ProductListDetailSerializer
from .models import Product


class ProductCreateListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    # serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListDetailSerializer
        return ProductSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     ean = self.request.query_params.get('ean_code')
    #     if ean is not None:
    #         queryset = queryset.filter(ean_code__icontains=ean)
    #     return queryset


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
