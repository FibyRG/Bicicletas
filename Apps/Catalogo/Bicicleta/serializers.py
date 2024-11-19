from rest_framework.serializers import ModelSerializer

from .models import Bicicleta


class BicicletaSerializer(ModelSerializer):
    class Meta:
        model = Bicicleta
        fields =[ 'CodigoDeBicicleta','DescripcionBicicleta','Grupo_Id','Marca_Id','AnioIngreso',
                     'PrecioCompra','Devaluacion','CostoAlquiler']
        #fields = '__all__'