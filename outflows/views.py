from .models import Outflow
from .serializers import OutflowSerializer, OutflowDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateOutflowAPIView(ListCreateAPIView):
    queryset = Outflow.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OutflowDetailSerializer
        return OutflowSerializer


class RetrieveUpdateDestroyOutflowAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Outflow.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OutflowDetailSerializer
        return OutflowSerializer
