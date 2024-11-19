from rest_framework.serializers import ModelSerializer

from .models import Marca

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = ['CodigoMarca', 'DescripcionMarca']
        #fields = '__all__'