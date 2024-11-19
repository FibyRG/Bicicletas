from django.urls import path

from .views import DatoAPIView, Datodetails

#app_name= "dato"

urlpatterns = [
    path("", DatoAPIView.as_view(), name="dato"),
 path('<int:pk>/', Datodetails.as_view())
]