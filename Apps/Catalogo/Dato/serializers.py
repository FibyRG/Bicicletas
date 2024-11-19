from rest_framework.serializers import ModelSerializer

from .models import Dato

class DatoSerializer(ModelSerializer):
    class Meta:
        model = Dato
        fields = ['Codigo','Nombres','Apellido1','Apellido2','Direccion','Telefono']
        #fields = '__all__'