from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from Apps.Catalogo.Empleado.models import Empleado
from Apps.Catalogo.Empleado.serializers import EmpleadoSerializer
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

class EmpleadoAPIView(PaginationMixin,APIView):
    """
    Vista para listar los empleados o crear un nuevo dato.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Empleado

    @swagger_auto_schema(responses={200: EmpleadoSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los Empleados.
        """
        logger.info("Petición GET para listar todos los empleados")
        empleado = Empleado.objects.all().order_by('id')
        page = self.paginate_queryset(empleado, request)

        if page is not None:
            serializer = EmoleadoSerializer(page, many=True)
            logger.info("Respuesta paginada para Empleado")
            return self.get_paginated_response(serializer.data)

        serializer = EmpleadoSerializer(empleado, many=True)
        logger.error("Mostrando todas los empleados sin paginación")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EmpleadoSerializer, responses={201: EmpleadoSerializer()})
    def post(self, request):
        """
        Crear un nuevo empleado.
        """
        logger.info("Petición POST para crear un nuevo empleado")
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("empleado creada exitosamente")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("No se pudo crear el empleado: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Empleadodetails(APIView):
    """
    Vista para obtener, actualizar o eliminar un empleado específico.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Empleado

    @swagger_auto_schema(responses={200: EmpleadoSerializer()})
    def get(self, request, pk):
        """
        Obtener un empleado específico por su ID.
        """
        try:
            empleado = Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            return Response({'error': 'empleado no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpleadoSerializer(empleado)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EmpleadoSerializer, responses={200: EmpleadoSerializer()})
    def put(self, request, pk):
        """
        Actualizar completamente un empleado por su ID.
        """
        logger.info("Solicitud PUT para actualizar el empleado con ID: %s", pk)
        try:
            empleado = Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            return Response({'error': 'empleado no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, empleado) #Verificación de permisos
        serializer = EmpleadoSerializer(empleado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("empleado actualizada exitosamente con ID: %s", pk)
            return Response(serializer.data)
        logger.error("No se pudo actualizar el cliente con ID: %s. Errors: %s",
                     pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=EmpleadoSerializer, responses={200: EmpleadoSerializer()})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un empleado por su ID.
        """
        logger.info("Solicitud PATCH para actualizar parcialmente un empleado con ID: %s", pk)
        try:
            empleado = Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            return Response({'error': 'empleado no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, empleado) #Verificación de permisos
        serializer = EmpleadoSerializer(empleado, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("empleado parcialmente actualizada exitosamente con ID: %s", pk)
            return Response(serializer.data)
        logger.error("No se pudo actualizar parcialmente el empleado con ID: %s. Errors: %s",
                     pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un empleado por su ID.
        """
        logger.info("Solicitud DELETE para eliminar un empleado con ID: %s", pk)
        try:
            empleado = Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            return Response({'error': 'empleado no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, empleado) #Verificación de permisos
        empleado.delete()
        logger.info("empleado eliminada exitosamente con ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)