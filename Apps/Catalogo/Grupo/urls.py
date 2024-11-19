from django.urls import path

from .views import GrupoAPIView, Grupodetails

#app_name= "grupo"

urlpatterns = [
    path("", GrupoAPIView.as_view(), name="grupo"),
 path('<int:pk>/', Grupodetails.as_view())
]