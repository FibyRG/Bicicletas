from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Marca
from .serializers import MarcaSerializer
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

class MarcaAPIView(PaginationMixin,APIView):
    """
    Vista para listar todas las marcas o crear un nuevo marca.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Marca

    @swagger_auto_schema(responses={200: MarcaSerializer(many=True)})
    def get(self, request):
        """
        Listar todas las marcas.
        """
        logger.info("Petición GET para listar todas las ")
        marca = Grupo.objects.all().order_by('id')
        page = self.paginate_queryset(marca, request)

        if page is not None:
            serializer = MarcaSerializer(page, many=True)
            logger.info("Respuesta paginada para Marcas")
            return self.get_paginated_response(serializer.data)

        serializer = MarcaSerializer(grupo, many=True)
        logger.error("Mostrando todas las marcas sin paginacion")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MarcaSerializer, responses={201: MarcaSerializer()})
    def post(self, request):
        """
        Crear un nuevo marca.
        """
        logger.info("Petición POST para crear una nueva marca")
        serializer = MarcaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("marca creada exitosamente")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("No se pudo crear la marca: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Marcadetails(APIView):
    """
    Vista para obtener, actualizar o eliminar una marca específica.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Marca

    @swagger_auto_schema(responses={200: MarcaSerializer()})
    def get(self, request, pk):
        """
        Obtener una marca específica por su ID.
        """
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response({'error': 'marca no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MarcaSerializer(marca)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MarcaSerializer, responses={200: MarcaSerializer()})
    def put(self, request, pk):
        """
        Actualizar completamente una marca por su ID.
        """
        logger.info("Solicitud PUT para actualizar una marca con ID: %s", pk)
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response({'error': 'marca no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, marca) #Verificación de permisos
        serializer = MarcaSerializer(marca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("marca actualizada exitosamente con ID: %s", pk)
            return Response(serializer.data)
        logger.error("No se pudo actualizar la marca con ID: %s. Errors: %s",
                     pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=MarcaSerializer, responses={200: MarcaSerializer()})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un marca por su ID.
        """
        logger.info("Solicitud PATCH para actualizar parcialmente una marca con ID: %s", pk)
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response({'error': 'marca no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, marca) #Verificación de permisos
        serializer = MarcaSerializer(marca, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("marca parcialmente actualizada exitosamente con ID: %s", pk)
            return Response(serializer.data)
        logger.error("No se pudo actualizar parcialmente la marca con ID: %s. Errors: %s",
                     pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una marca por su ID.
        """
        logger.info("Solicitud DELETE para eliminar una marca con ID: %s", pk)
        try:
            marca = Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            return Response({'error': 'marca no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, marca) #Verificación de permisos
        marca.delete()
        logger.info("marca eliminada exitosamente con ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)