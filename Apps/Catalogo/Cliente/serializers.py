from rest_framework.serializers import ModelSerializer

from .models import Cliente


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields =[  'CodigoCliente', 'Dato_Id']
        #fields = '__all__'