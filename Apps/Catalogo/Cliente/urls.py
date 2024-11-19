from django.urls import path

from .views import ClienteAPIView, Clientedetails

#app_name= "cliente"

urlpatterns = [
    path("", ClienteAPIView.as_view(), name="cliente"),
 path('<int:pk>/', Clientedetails.as_view())
]