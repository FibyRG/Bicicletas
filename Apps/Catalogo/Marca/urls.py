from django.urls import path

from .views import MarcaAPIView, Marcadetails

#app_name= "marca"

urlpatterns = [
    path("", MarcaAPIView.as_view(), name="marca"),
 path('<int:pk>/', Marcadetails.as_view())
]