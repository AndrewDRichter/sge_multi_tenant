from django.http import HttpResponse
from .models import Entity
from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.decorators import login_required
from .serializers import EntitySerializer, UserSerializer
from django.db.utils import IntegrityError


class ListCreateEntityAPIView(ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class ListCreateUserAPIView(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        User = get_user_model()
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError as e:
            return HttpResponse({'Error': 'User already exists'})
        return HttpResponse(user)


@login_required
def index(request):
    user = request.user
    return HttpResponse(f'<h1>Homepage {user}</h1>')
