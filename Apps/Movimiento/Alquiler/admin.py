from django.contrib import admin

from Apps.Movimiento.Alquiler.models import Alquiler, DetalleAlquiler


@admin.register(Alquiler)
# Register your models here.

class AlquilerAdmin(admin.ModelAdmin):
    list_display = [ 'FechaAlquiler','Descripcion','CodigoAlquiler','Cliente_Id','Empleado_Id']
    search_fields = ['Descripcion']
# Register your models here.

@admin.register(DetalleAlquiler)
class DetalleAlquilerAdmin(admin.ModelAdmin):
    list_display = ['Bicicleta_Id','Alquiler_Id','FechaAlquiler','FechaDevolucion',
                    'FechaRealDevolucion','Costo','Cantidad']
    search_fields = ['Alquiler_Id']

