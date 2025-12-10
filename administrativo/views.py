from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import Rol,User
from .serializers import RolSerializer
from .serializers import RolSerializer, UserSerializer
# Create your views here.


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

