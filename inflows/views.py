from rest_framework import generics
from inflows.serializers import InflowSerializer
from .models import Inflow


class InflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer


class InflowRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer
