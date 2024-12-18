# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Empleado
# from .serializers import EmpleadoSerializer

# class DetalleRepuestoApiView(APIView):
#
#     def get(self, request, pk=None):
#         """
#         Obtener un departamento específico (si se proporciona pk) o todos las bicicletas.
#         """
#         if pk:
#             try:
#                 empleado = Empleado.objects.get(pk=pk)
#             except Empleado.DoesNotExist:
#                 return Response({'error': 'empleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)
#             serializer =EmpleadoSerializer(empleado)
#             return Response(serializer.data)
#         else:
#             empleado = Empleado.objects.all()
#             serializer = EmpleadoSerializer(empleado, many=True)
#             return Response(serializer.data)
#
#     def post(self, request):
#         """
#         Crear un nuevo empleado.
#         """
#         serializer = EmpleadoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None):
#         """
#         Actualizar un empleado existente completamente.
#         """
#         try:
#             empleado = Empleado.objects.get(pk=pk)
#         except Empleado.DoesNotExist:
#             return Response({'error': 'empleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = EmpleadoSerializer(empleado, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk=None):
#         """
#         Actualización parcial del empleado.
#         """
#         try:
#             empleado = Empleado.objects.get(pk=pk)
#         except Empleado.DoesNotExist:
#             return Response({'error': 'empleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = EmpleadoSerializer(empleado, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk=None):
#         """
#         Eliminar un empleado.
#         """
#         try:
#             empleado = Empleado.objects.get(pk=pk)
#         except Empleado.DoesNotExist:
#             return Response({'error': 'empleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)
#
#         empleado.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from django.urls import path
# from .views import DepartamentoApiView
#
# urlpatterns = [
#     path('departamentos/', DepartamentoApiView.as_view()),  # Para listar o crear departamentos
#     path('departamentos/<int:pk>/', DepartamentoApiView.as_view()),  # Para operaciones GET, PUT, PATCH, DELETE
# ]