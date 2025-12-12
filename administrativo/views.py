from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import Rol,User, Client, Cobrador, Prestamo, Cuota, Pago
from .serializers import RolSerializer, UserSerializer, ClientSerializer, CobradorSerializer, PrestamoSerializer, CuotaSerializer, PagoSerializer
# Create your views here.


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CobradorViewSet(viewsets.ModelViewSet):
    queryset = Cobrador.objects.all()
    serializer_class = CobradorSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class CuotaViewSet(viewsets.ModelViewSet):
    queryset = Cuota.objects.all()
    serializer_class = CuotaSerializer
    
class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer