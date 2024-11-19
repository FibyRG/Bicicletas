from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bicicleta
from .serializers import BicicletaSerializer

class AlquilerApiView(APIView):

    def get(self, request, pk=None):
        """
        Obtener un departamento específico (si se proporciona pk) o todos las bicicletas.
        """
        if pk:
            try:
                bicicletas = Bicicleta.objects.get(pk=pk)
            except Bicicleta.DoesNotExist:
                return Response({'error': 'bicicletas no encontrado'}, status=status.HTTP_404_NOT_FOUND)
            serializer =BicicletaSerializer(bicicletas)
            return Response(serializer.data)
        else:
            bicicletas = Bicicleta.objects.all()
            serializer = BicicletaSerializer(bicicletas, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Crear un nuevo alquiler.
        """
        serializer = BicicletaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Actualizar una bicicleta existente completamente.
        """
        try:
            bicicletas = Bicicleta.objects.get(pk=pk)
        except Bicicleta.DoesNotExist:
            return Response({'error': 'bicicleta no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BicicletaSerializer(bicicletas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """
        Actualización parcial de una bicicleta.
        """
        try:
            biciletas = Bicicleta.objects.get(pk=pk)
        except Bicicleta.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BicicletaSerializer(biciletas, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
        Eliminar un alquiler.
        """
        try:
            bicicletas = Bicicleta.objects.get(pk=pk)
        except Bicicleta.DoesNotExist:
            return Response({'error': 'Bicicleta no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        bicicletas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from django.urls import path
# from .views import DepartamentoApiView
#
# urlpatterns = [
#     path('departamentos/', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
#     path('departamentos/<int:pk>/', DepartamentoApiView.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
# ]