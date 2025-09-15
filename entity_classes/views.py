from .models import EntityClass
from rest_framework.generics import ListAPIView
from .serializers import EntityClassSerializer
from rest_framework.permissions import AllowAny


class ListEntityClassesAPIView(ListAPIView):
    queryset = EntityClass.objects.all()
    serializer_class = EntityClassSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
