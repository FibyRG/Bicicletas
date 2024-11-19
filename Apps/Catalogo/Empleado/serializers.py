from rest_framework.serializers import ModelSerializer

from .models import Empleado


class EmpleadoSerializer(ModelSerializer):
    class Meta:
        model = Empleado
        fields =[ 'Dato_Id','Salario']
        #fields = '__all__'