from django.urls import path, include

urlpatterns = [
path('alquileres/', include('Apps.Movimiento.Alquiler.urls')),

path('reparaciones/', include('Apps.Movimiento.Reparacion.urls')),


]