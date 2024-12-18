from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Marca
from .serializers import MarcaSerializer

class MarcaApiView(APIView):

    def get(self, request, pk=None):
        """
        Obtener un departamento específico (si se proporciona pk) o todas las marcas.
        """
        if pk:
            try:
                marcas = Marca.objects.get(pk=pk)
            except Marca.DoesNotExist:
                return Response({'error': 'Marca no encontrado'}, status=status.HTTP_404_NOT_FOUND)
            serializer = MarcaSerializer(marcas)
            return Response(serializer.data)
        else:
            marca = Marca.objects.all()
            serializer = Marca(marca, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Crear una nuevo Marca.
        """
        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Actualizar una marca existente completamente.
        """
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response({'error': 'Marca no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MarcaSerializer(Marca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """
        Actualización parcial de un departamento.
        """
        try:
            dato = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MarcaSerializer(dato, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
        Eliminar una marca.
        """
        try:
            dato = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response({'error': 'Marca no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        dato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from django.urls import path
# from .views import DepartamentoApiView
#
# urlpatterns = [
#     path('departamentos/', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
#     path('departamentos/<int:pk>/', DepartamentoApiView.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
# ]