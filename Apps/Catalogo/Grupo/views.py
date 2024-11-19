from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Grupo
from .serializers import GrupoSerializer
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

class GrupoAPIView(PaginationMixin,APIView):
    """
    Vista para listar todos los grupos o crear un nuevo grupo.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Grupo

    @swagger_auto_schema(responses={200: GrupoSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los Grupos.
        """
        logger.info("Petición GET para listar todos los grupos")
        grupo = Grupo.objects.all().order_by('id')
        page = self.paginate_queryset(grupo, request)

        if page is not None:
            serializer = GrupoSerializer(page, many=True)
            logger.info("Respuesta paginada para Grupo")
            return self.get_paginated_response(serializer.data)

        serializer = GrupoSerializer(grupo, many=True)
        logger.error("Mostrando todas los grupo sin paginación")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=GrupoSerializer, responses={201: GrupoSerializer()})
    def post(self, request):
        """
        Crear un nuevo grupo.
        """
        logger.info("Petición POST para crear un nuevo grupo")
        serializer = GrupoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("grupo creada exitosamente")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("No se pudo crear el grupo: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Grupodetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un grupo específico.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Grupo

    @swagger_auto_schema(responses={200: GrupoSerializer()})
    def get(self, request, pk):
        """
        Obtener un grupo específico por su ID.
        """
        try:
            grupo = Grupo.objects.get(pk=pk)
        except Grupo.DoesNotExist:
            return Response({'error': 'grupo no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = GrupoSerializer(grupo)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=GrupoSerializer, responses={200: GrupoSerializer()})
    def put(self, request, pk):
        """
        Actualizar completamente un grupo por su ID.
        """
        logger.info("Solicitud PUT para actualizar el grupo con ID: %s", pk)
        try:
            grupo = Grupo.objects.get(pk=pk)
        except Grupo.DoesNotExist:
            return Response({'error': 'grupo no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, grupo) #Verificación de permisos
        serializer = GrupoSerializer(grupo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("grupo actualizada exitosamente con ID: %s", pk)
            return Response(serializer.data)
        logger.error("No se pudo actualizar el grupo con ID: %s. Errors: %s",
                     pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=GrupoSerializer, responses={200: GrupoSerializer()})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un grupo por su ID.
        """
        logger.info("Solicitud PATCH para actualizar parcialmente un grupo con ID: %s", pk)
        try:
            grupo = Grupo.objects.get(pk=pk)
        except Grupo.DoesNotExist:
            return Response({'error': 'grupo no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, grupo) #Verificación de permisos
        serializer = GrupoSerializer(grupo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("grupo parcialmente actualizada exitosamente con ID: %s", pk)
            return Response(serializer.data)
        logger.error("No se pudo actualizar parcialmente el grupo con ID: %s. Errors: %s",
                     pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un grupo por su ID.
        """
        logger.info("Solicitud DELETE para eliminar un grupo con ID: %s", pk)
        try:
            grupo = Grupo.objects.get(pk=pk)
        except Grupo.DoesNotExist:
            return Response({'error': 'grupo no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, grupo) #Verificación de permisos
        grupo.delete()
        logger.info("grupo eliminada exitosamente con ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)