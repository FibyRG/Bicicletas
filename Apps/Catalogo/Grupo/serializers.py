from rest_framework.serializers import ModelSerializer

from .models import Grupo

class GrupoSerializer(ModelSerializer):
    class Meta:
        model = Grupo
        fields = ['CodigoGrupo', 'DescripcionGrupo']
        #fields = '__all__'