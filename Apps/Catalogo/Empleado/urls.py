from django.urls import path

from .views import EmpleadoAPIView, Empleadodetails

#app_name= "empleado"

urlpatterns = [
    path("", EmpleadoAPIView.as_view(), name="empleado"),
 path('<int:pk>/', Empleadodetails.as_view())
]