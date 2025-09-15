import json
from django.http import HttpResponse, JsonResponse
from .serializers import UserSerializer
from django.db.utils import IntegrityError
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import get_user_model


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
            #TODO: Testar o JsonResponse em vez do HTTPResponse
            return JsonResponse({'Error': 'User already exists'})
        return JsonResponse(json.dump(user))