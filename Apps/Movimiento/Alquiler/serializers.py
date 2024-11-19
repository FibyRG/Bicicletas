from rest_framework import serializers
from .models import Alquiler, DetalleAlquiler
from Apps.Catalogo.Cliente.models import Cliente
from Apps.Catalogo.Empleado.models import Empleado
from Apps.Catalogo.Dato.models import Dato
from Apps.Catalogo.Bicicleta.models import Bicicleta

class DetalleAlquilerSerializer(serializers.ModelSerializer):
    Alquiler_Id = serializers.PrimaryKeyRelatedField(read_only=True)
    FechaAlquiler = serializers.DateTimeField(read_only=True)
    Bicicleta_Descripcion = serializers.CharField(source='Bicicleta_Id.DescripcionBicicleta', read_only=True)

    class Meta:
        model = DetalleAlquiler
        fields = [
            'Bicicleta_Id', 'Bicicleta_Descripcion', 'Alquiler_Id', 'FechaAlquiler',
            'FechaDevolucion', 'FechaRealDevolucion', 'Costo', 'Cantidad'
        ]
        read_only_fields = ['Alquiler_Id', 'FechaAlquiler']

class AlquilerSerializer(serializers.ModelSerializer):
    DetallesAlquiler = DetalleAlquilerSerializer(many=True)
    Cliente_Nombre = serializers.CharField(source='Cliente_Id.Dato_Id.Nombres', read_only=True)
    Empleado_Nombre = serializers.CharField(source='Empleado_Id.Dato_Id.Nombres', read_only=True)

    class Meta:
        model = Alquiler
        fields = [
            'FechaAlquiler', 'Descripcion', 'CodigoAlquiler', 'Cliente_Id', 'Cliente_Nombre',
            'Empleado_Id', 'Empleado_Nombre', 'DetallesAlquiler'
        ]
        read_only_fields = ['FechaAlquiler']
