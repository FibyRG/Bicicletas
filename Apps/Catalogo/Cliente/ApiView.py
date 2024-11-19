from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteApiView(APIView):

    def get(self, request, pk=None):
        """
        Obtener un departamento específico (si se proporciona pk) o todos las bicicletas.
        """
        if pk:
            try:
                clientes = Cliente.objects.get(pk=pk)

            except Cliente.DoesNotExist:
                return Response({'error': 'cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)
            serializer =ClienteSerializer(clientes)
            print(serializer.data)
            return Response(serializer.data)
        else:
            clientes = Cliente.objects.all()
            serializer = ClienteSerializer(clientes, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Crear un nuevo Cliente.
        """
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Actualizar un cliente existente completamente.
        """
        try:
            clientes = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'clientes no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClienteSerializer(clientes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """
        Actualización parcial del cliente.
        """
        try:
            clientes = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClienteSerializer(clientes, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
        Eliminar un Cliente.
        """
        try:
            clientes = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        clientes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from django.urls import path
# from .views import DepartamentoApiView
#
# urlpatterns = [
#     path('departamentos/', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
#     path('departamentos/<int:pk>/', DepartamentoApiView.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
# ]