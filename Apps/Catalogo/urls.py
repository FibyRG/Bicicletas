from django.urls import path, include

urlpatterns = [
path('dato/', include('Apps.Catalogo.Dato.urls')),

path('Empleado/', include('Apps.Catalogo.Empleado.urls')),
#
path('Cliente/', include('Apps.Catalogo.Cliente.urls')),
#
path('grupos/', include('Apps.Catalogo.Grupo.urls')),
#
path('marcas/', include('Apps.Catalogo.Marca.urls')),
#
path('bicicletas/', include('Apps.Catalogo.Bicicleta.urls')),

]