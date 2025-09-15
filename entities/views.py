from .models import Entity
from .serializers import EntitySerializer, EntityDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateEntityAPIView(ListCreateAPIView):
    queryset = Entity.objects.all()
    # serializer_class = EntitySerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EntityDetailSerializer
        return EntitySerializer


class RetrieveUpdateDestroyEntityAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Entity.objects.all()
    # serializer_class = EntitySerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EntityDetailSerializer
        return EntitySerializer
