from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dato
from .serializers import DatoSerializer

class DatoApiView(APIView):

    def get(self, request, pk=None):
        """
        Obtener un departamento específico (si se proporciona pk) o todos los datos.
        """
        if pk:
            try:
                dato = Dato.objects.get(pk=pk)
            except Dato.DoesNotExist:
                return Response({'error': 'Dato no encontrado'}, status=status.HTTP_404_NOT_FOUND)
            serializer = DatoSerializer(dato)
            return Response(serializer.data)
        else:
            datos = Dato.objects.all()
            serializer = DatoSerializer(datos, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Crear un nuevo dato.
        """
        serializer = DatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Actualizar un dato existente completamente.
        """
        try:
            dato = Dato.objects.get(pk=pk)
        except Dato.DoesNotExist:
            return Response({'error': 'Dato no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DatoSerializer(dato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """
        Actualización parcial de un departamento.
        """
        try:
            dato = Dato.objects.get(pk=pk)
        except Dato.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DatoSerializer(dato, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
        Eliminar un dato.
        """
        try:
            dato = Dato.objects.get(pk=pk)
        except Dato.DoesNotExist:
            return Response({'error': 'Dato no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        dato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from django.urls import path
# from .views import DepartamentoApiView
#
# urlpatterns = [
#     path('departamentos/', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
#     path('departamentos/<int:pk>/', DepartamentoApiView.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
# ]