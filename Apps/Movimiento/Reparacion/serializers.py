from rest_framework.serializers import ModelSerializer

from .models import DetalleReparacion , Reparacion


class ReparacionSerializer(ModelSerializer):
    class Meta:
        model = Reparacion
        fields = ['CodigoReparacion', 'DescripcionReparacion','Costo']
        #fields = '__all__'


class DetalleReparacionSerializer(ModelSerializer):
    class Meta:
        model = DetalleReparacion
        fields =[ 'BicicletaId','ReparacionId','FechaReparacion','CostoReparacion',
                     'Observaciones']
        #fields = '__all__'