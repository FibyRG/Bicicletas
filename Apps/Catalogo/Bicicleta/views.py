from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Bicicleta
from .serializers import BicicletaSerializer
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

class BicicletaAPIView(PaginationMixin,APIView):
    """
    Vista para listar toda la bicicleta o crear una nueva unidad de medida.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Bicicleta

    @swagger_auto_schema(responses={200: BicicletaSerializer(many=True)})
    def get(self, request):
        """
        Listar todas las unidades de medida.
        """
        logger.info("Peticion GET para listar todas las bicicletas ")
        bicicleta = Bicicleta.objects.all().order_by('id')
        page = self.paginate_queryset(bicicleta, request)

        if page is not None:
            serializer = UnidadMedidaSerializer(page, many=True)
            logger.info("Respuesta paginada para unidad_medida")
            return self.get_paginated_response(serializer.data)

        serializer = BicicletaSerializer(bicicleta, many=True)
        logger.error("Mostrando todas las bicicletas sin paginacion")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BicicletaSerializer, responses={201: BicicletaSerializer()})
    def post(self, request):
        """
        Crear una nueva unidad de medida.
        """
        logger.info("Peticicion POST para crear una nueva unidad de medida")
        serializer = BicicletaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("bicicleta creada exitosamente")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("No se pudo crear la bicicleta: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Bicicletadetails(APIView):
    """
    Vista para obtener, actualizar o eliminar una biciceta específica.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Bicicleta

    @swagger_auto_schema(responses={200: BicicletaSerializer()})
    def get(self, request, pk):
        """
        Obtener una unidad de bicicleta específica por su ID.
        """
        try:
            bicicleta = Bicicleta.objects.get(pk=pk)
        except Bicicleta.DoesNotExist:
            return Response({'error': 'bicicleta no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BicicletaSerializer(bicicleta)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BicicletaSerializer, responses={200: BicicletaSerializer()})
    def put(self, request, pk):
        """
        Actualizar completamente una bicicleta por su ID.
        """
        logger.info("Solicitud PUT para actualizar la bicicleta con ID: %s", pk)
        bicicleta = get_object_or_404(bicicleta, id=pk)
        try:
            bicicleta = Bicicleta.objects.get(pk=pk)
        except Bicicleta.DoesNotExist:
            return Response({'error': 'Bicicleta no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        #self.check_object_permissions(request, bicicleta) #Verificación de permisos
        serializer = BicicletaSerializer(bicicleta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("bicicleta actualizada exitosamente con ID: %s", pk)
            return Response(serializer.data)
        logger.error("No se pudo actualizar la bicicleta con ID: %s. Errors: %s",
                     pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=BicicletaSerializer, responses={200: BicicletaSerializer()})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una bicicleta por su ID.
        """
        logger.info("Solicitud PATCH para actualizar parcialmente la bicicleta con ID: %s", pk)
        try:
            bicicleta = Bicicleta.objects.get(pk=pk)
        except Bicicleta.DoesNotExist:
            return Response({'error': 'bicicleta no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, bicicleta) #Verificación de permisos
        serializer = BicicletaSerializer(bicicleta, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Bicicleta parcialmente actualizada exitosamente con ID: %s", pk)
            return Response(serializer.data)
        logger.error("No se pudo actualizar parcialmente la bicicleta con ID: %s. Errors: %s",
                     pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una bicicleta por su ID.
        """
        logger.info("Solicitud DELETE para eliminar una bicicleta con ID: %s", pk)
        try:
            bicicleta = Bicicleta.objects.get(pk=pk)
        except Bicicleta.DoesNotExist:
            return Response({'error': 'bicicleta no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, bicicleta) #Verificación de permisos
        bicicleta.delete()
        logger.info("bicicleta eliminada exitosamente con ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)