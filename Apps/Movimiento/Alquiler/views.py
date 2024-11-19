from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.db import transaction
from .serializers import AlquilerSerializer, DetalleAlquilerSerializer
from .models import Alquiler, DetalleAlquiler
from drf_yasg.utils import swagger_auto_schema
from Apps.seguridad.permissions import *
from config.Utils.Pagination import *
from rest_framework.permissions import IsAuthenticated
from Apps.seguridad.permissions import CustomPermission

"""
    Endpoint de Alquiler
"""


class AlquilerCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Alquiler  # Aquí definimos el modelo explícitamente
    @swagger_auto_schema(request_body=AlquilerSerializer, responses={200: AlquilerSerializer})
    def post(self, request):
        serializer = AlquilerSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    detalles_data = serializer.validated_data.pop('DetallesAlquiler')
                    alquiler = Alquiler.objects.create(**serializer.validated_data)

                    for detalle_data in detalles_data:
                        DetalleAlquiler.objects.create(
                            Alquiler_Id=alquiler,
                            **detalle_data
                        )

                    alquiler_serializado = AlquilerSerializer(alquiler)
                    return Response(alquiler_serializado.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlquilerListAPIView(APIView):


    permission_classes = [IsAuthenticated, CustomPermission]
    model = Alquiler  # Aquí definimos el modelo explícitamente

    @swagger_auto_schema(
        operation_summary="Listar todos los alquileres",
        responses={200: AlquilerSerializer(many=True)}
    )
    def get(self, request):
        alquileres = Alquiler.objects.all()
        serializer = AlquilerSerializer(alquileres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AlquilerDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Alquiler  # Aquí definimos el modelo explícitamente
    @swagger_auto_schema(
        operation_summary="Obtener un alquiler específico por ID",
        responses={200: AlquilerSerializer, 404: 'Not Found'}
    )
    def get(self, request, pk):
        alquiler = get_object_or_404(Alquiler, pk=pk)
        serializer = AlquilerSerializer(alquiler)
        return Response(serializer.data, status=status.HTTP_200_OK)





