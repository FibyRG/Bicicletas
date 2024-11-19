from django.urls import path

from Apps.Movimiento.Reparacion.views import ReparacionCreateAPIView

#app_name= 'reparaciones'

urlpatterns = [
    path("", ReparacionCreateAPIView.as_view(), name="reparaciones"),
]