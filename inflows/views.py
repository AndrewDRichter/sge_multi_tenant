from rest_framework import generics
from inflows.serializers import InflowSerializer, InflowDetailSerializer
from .models import Inflow


class InflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = Inflow.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InflowDetailSerializer
        return InflowSerializer


class InflowRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inflow.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InflowDetailSerializer
        return InflowSerializer
