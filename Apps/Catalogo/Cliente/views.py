from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Cliente
from .serializers import ClienteSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from Apps.seguridad.permissions import *
from config.Utils.Pagination import *
import logging.handlers
from rest_framework.permissions import IsAuthenticated
from Apps.seguridad.permissions import CustomPermission

"""------------------------------------------------------------------------------"""

# Configura el logger
logger = logging.getLogger(__name__)

class ClienteAPIView(PaginationMixin,APIView):
    """
    Vista para listar todos los clientes o crear un nuevo dato.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Cliente

    @swagger_auto_schema(responses={200: ClienteSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los clientes.
        """
        logger.info("Peticion GET para listar todas los clientes ")
        cliente = Cliente.objects.all().order_by('id')
        page = self.paginate_queryset(cliente, request)

        if page is not None:
            serializer = ClienteSerializer(page, many=True)
            logger.info("Respuesta paginada para cliente")
            return self.get_paginated_response(serializer.data)

        serializer = ClienteSerializer(cliente, many=True)
        logger.error("Mostrando todos los clientes sin paginacion")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ClienteSerializer, responses={201: ClienteSerializer()})
    def post(self, request):
        """
        Crear un nuevo cliente.
        """
        logger.info("Peticicion POST para crear una nueva cliente")
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("cliente creada exitosamente")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("No se pudo crear el cliente: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Clientedetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un cliente específica.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Cliente

    @swagger_auto_schema(responses={200: ClienteSerializer()})
    def get(self, request, pk):
        """
        Obtener una unidad de cliente específica por su ID.
        """
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'cliente no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ClienteSerializer, responses={200: ClienteSerializer()})
    def put(self, request, pk):
        """
        Actualizar completamente una cliente por su ID.
        """
        logger.info("Solicitud PUT para actualizar el cliente con ID: %s", pk)
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'cliente no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, cliente) #Verificación de permisos
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("cliente actualizada exitosamente con ID: %s", pk)
            return Response(serializer.data)
        logger.error("No se pudo actualizar el cliente con ID: %s. Errors: %s",
                     pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ClienteSerializer, responses={200: ClienteSerializer()})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un cliente por su ID.
        """
        logger.info("Solicitud PATCH para actualizar parcialmente el cliente con ID: %s", pk)
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'cliente no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, cliente) #Verificación de permisos
        serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("cliente parcialmente actualizada exitosamente con ID: %s", pk)
            return Response(serializer.data)
        logger.error("No se pudo actualizar parcialmente el cliente con ID: %s. Errors: %s",
                     pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un cliente por su ID.
        """
        logger.info("Solicitud DELETE para eliminar una cliente con ID: %s", pk)
        try:
            cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'error': 'cliente no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, cliente) #Verificación de permisos
        cliente.delete()
        logger.info("cliente eliminada exitosamente con ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)