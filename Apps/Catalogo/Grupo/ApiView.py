from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Grupo
from .serializers import GrupoSerializer

class GrupoApiView(APIView):

    def get(self, request, pk=None):
        """
        Obtener un departamento específico (si se proporciona pk) o todos los Grupos.
        """
        if pk:
            try:
                grupos = Grupo.objects.get(pk=pk)
            except Grupo.DoesNotExist:
                return Response({'error': 'Grupo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
            serializer = Grupo(grupos)
            return Response(serializer.data)
        else:
            Grupos = Grupo.objects.all()
            serializer = GrupoSerializer(Grupos, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Crear un nuevo grupo.
        """
        serializer = GrupoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Actualizar un Grupo existente completamente.
        """
        try:
            grupos = Grupo.objects.get(pk=pk)
        except Grupo.DoesNotExist:
            return Response({'error': 'Dato no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = Grupo(grupos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """
        Actualización parcial de un Grupo.
        """
        try:
            grupos = Grupo.objects.get(pk=pk)
        except Grupo.DoesNotExist:
            return Response({'error': 'Grupo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = GrupoSerializer(grupos, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """
        Eliminar un Grupo.
        """
        try:
            grupos = Grupo.objects.get(pk=pk)
        except Grupo.DoesNotExist:
            return Response({'error': 'Grupo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        grupos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from django.urls import path
# from .views import DepartamentoApiView
#
# urlpatterns = [
#     path('departamentos/', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
#     path('departamentos/<int:pk>/', DepartamentoApiView.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
# ]