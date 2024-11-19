from django.urls import path

from .views import *

app_name= "alquileres"

urlpatterns = [
   path('alquileres/', AlquilerListAPIView.as_view(), name='alquiler-list'),
    path('alquileres/crear/', AlquilerCreateAPIView.as_view(), name='alquiler-create'),
    path('alquileres/<int:pk>/', AlquilerDetailAPIView.as_view(), name='alquiler-detail'),
]