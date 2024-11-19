from django.urls import path

from .views import BicicletaAPIView, Bicicletadetails

#app_name= "bicicletas"

urlpatterns = [
    path("", BicicletaAPIView.as_view(), name="bicicletas"),
 path('<int:pk>/', Bicicletadetails.as_view())
]