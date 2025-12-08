from rest_framework import serializers
from inteligencia_artificial.administrativo.models import Rol

class RolSerializar(serializers.ModelSerializer):
    class Meta:
        model = Rol 
        fields = '__all__'