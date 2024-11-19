from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.db import transaction
from .serializers import ReparacionSerializer, DetalleReparacionSerializer
from .models import Reparacion, DetalleReparacion
from drf_yasg.utils import swagger_auto_schema
from Apps.seguridad.permissions import *
from config.Utils.Pagination import *
from rest_framework.permissions import IsAuthenticated
from Apps.seguridad.permissions import CustomPermission

"""
    Endpoint de Reparacion
"""


class ReparacionCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Reparacion  # Aquí definimos el modelo explícitamente
    @swagger_auto_schema(request_body=ReparacionSerializer, responses={200: ReparacionSerializer})
    def post(self, request):
        serializer = ReparacionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    detalles_data = serializer.validated_data.pop('DetalleReparacion')
                    reparacion = Alquiler.objects.create(**serializer.validated_data)

                    for detalle_data in detalles_data:
                        DetalleAlquiler.objects.create(
                            ReparacionId=reparacion,
                            **detalle_data
                        )

                    reparaciones = ReparacionSerializer(reparaciones)
                    return Response(reparaciones.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReparacionListAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Listar todos los reparaciones",
        responses={200: ReparacionSerializer(many=True)}
    )
    def get(self, request):
        reparaciones = Reparacion.objects.all()
        serializer = ReparacionSerializer(reparaciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReparacionDetailAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="Obtener una reparacion específico por ID",
        responses={200: ReparacionSerializer, 404: 'Not Found'}
    )
    def get(self, request, pk):
        reparaciones = get_object_or_404(Alquiler, pk=pk)
        serializer = ReparacionSerializer(reparaciones)
        return Response(serializer.data, status=status.HTTP_200_OK)





