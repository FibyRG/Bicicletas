from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Dato
from .serializers import DatoSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from Apps.seguridad.permissions import *
from config.Utils.Pagination import *
import logging.handlers
from rest_framework.permissions import IsAuthenticated
from Apps.seguridad.permissions import CustomPermission

# Configura el logger
logger = logging.getLogger(__name__)
"""------------------------------------------------------------------------------"""

class DatoAPIView(PaginationMixin,APIView):
    """
    Vista para listar todos los datos o crear un nuevo dato.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Dato

    @swagger_auto_schema(responses={200: DatoSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los datos.
        """
        logger.info("Petición GET para listar todos los datos")
        dato = Dato.objects.all().order_by('id')
        page = self.paginate_queryset(cliente, request)

        if page is not None:
            serializer = DatoSerializer(page, many=True)
            logger.info("Respuesta paginada para Dato")
            return self.get_paginated_response(serializer.data)

        serializer = DatoSerializer(dato, many=True)
        logger.error("Mostrando todos los dato sin paginación")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DatoSerializer, responses={201: DatoSerializer()})
    def post(self, request):
        """
        Crear un nuevo dato.
        """
        logger.info("Petición POST para crear una nueva dato")
        serializer = DatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("dato creada exitosamente")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("No se pudo crear el dato: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Datodetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un dato específica.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Dato

    @swagger_auto_schema(responses={200: DatoSerializer()})
    def get(self, request, pk):
        """
        Obtener una unidad de dato específica por su ID.
        """
        try:
            dato = Dato.objects.get(pk=pk)
        except Dato.DoesNotExist:
            return Response({'error': 'dato no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DatoSerializer(dato)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DatoSerializer, responses={200: DatoSerializer()})
    def put(self, request, pk):
        """
        Actualizar completamente un dato por su ID.
        """
        logger.info("Solicitud PUT para actualizar el dato con ID: %s", pk)
        try:
            dato = Dato.objects.get(pk=pk)
        except Dato.DoesNotExist:
            return Response({'error': 'dato no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, dato) #Verificación de permisos
        serializer = DatoSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("dato actualizada exitosamente con ID: %s", pk)
            return Response(serializer.data)
        logger.error("No se pudo actualizar el dato con ID: %s. Errors: %s",
                     pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=DatoSerializer, responses={200: DatoSerializer()})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un dato por su ID.
        """
        logger.info("Solicitud PATCH para actualizar parcialmente un dato con ID: %s", pk)
        try:
            dato = Dato.objects.get(pk=pk)
        except Dato.DoesNotExist:
            return Response({'error': 'dato no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, dato) #Verificación de permisos
        serializer = DatoSerializer(dato, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("dato parcialmente actualizada exitosamente con ID: %s", pk)
            return Response(serializer.data)
        logger.error("No se pudo actualizar parcialmente el dato con ID: %s. Errors: %s",
                     pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un dato por su ID.
        """
        logger.info("Solicitud DELETE para eliminar un dato con ID: %s", pk)
        try:
            dato = Dato.objects.get(pk=pk)
        except Dato.DoesNotExist:
            return Response({'error': 'dato no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, dato) #Verificación de permisos
        dato.delete()
        logger.info("dato eliminada exitosamente con ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)