from rest_framework import serializers
from .models import Rol, User, Client, Cobrador, Prestamo, Cuota, Pago

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol 
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    rol_id = serializers.PrimaryKeyRelatedField(
        queryset = Rol.objects.all(),
        source = 'rol', 
        write_only = True
        )
    rol = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = User
        fields = ['id', 'username', 'foto', 'correo', 'rol_id', 'rol']
        extra_kwargs ={'password': {'write_only': True}}

class ClientSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = 'user', 
        write_only = True
        )
    user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Client
        fields = ['id', 'nombre', 'apellido', 'cedulaIdentidad', 'direccion', 'telefono', 'email', 'user_id', 'user']

class CobradorSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),
        source = 'user', 
        write_only = True
        )
    user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Cobrador
        fields = ['id', 'nombre', 'apellido', 'cedulaIdentidad', 'telefono', 'email', 'user_id', 'user']

class PrestamoSerializer(serializers.ModelSerializer):
    client_id = serializers.PrimaryKeyRelatedField(
        queryset = Client.objects.all(),
        source = 'client', 
        write_only = True
        )
    client = serializers.StringRelatedField(read_only = True)
    cobrador_id = serializers.PrimaryKeyRelatedField(
        queryset = Cobrador.objects.all(),
        source = 'cobrador', 
        write_only = True
        )
    cobrador = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Prestamo
        fields = ['id', 'monto', 'tasa_interes', 'plazo', 'fecha_inicio', 'fecha_fin', 'estado', 'client_id', 'client', 'cobrador_id', 'cobrador']

class CuotaSerializer(serializers.ModelSerializer):
    prestamo_id = serializers.PrimaryKeyRelatedField(
        queryset = Prestamo.objects.all(),
        source = 'prestamo', 
        write_only = True
        )
    prestamo = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Cuota
        fields = ['id', 'numero_cuota', 'monto', 'fecha_vencimiento', 'estado', 'prestamo_id', 'prestamo']

class PagoSerializer(serializers.ModelSerializer):
    cuota_id = serializers.PrimaryKeyRelatedField(
        queryset = Cuota.objects.all(),
        source = 'cuota', 
        write_only = True
        )
    cuota = serializers.StringRelatedField(read_only = True)
    cobrador_id = serializers.PrimaryKeyRelatedField(
        queryset = Cobrador.objects.all(),
        source = 'cobrador', 
        write_only = True
        )
    cobrador = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Pago
        fields = ['id', 'monto', 'fecha_pago', 'metodo_pago', 'cuota_id', 'cuota', 'cobrador_id', 'cobrador']

