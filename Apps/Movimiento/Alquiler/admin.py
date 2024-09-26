from django.contrib import admin

from Apps.Movimiento.Alquiler.models import Alquiler


@admin.register(Alquiler)
# Register your models here.

class AlquilerAdmin(admin.ModelAdmin):
    list_display = [ 'FechaAlquiler','Descripcion','CodigoAlquiler','Cliente_Id','Empleado_Id']
    search_fields = ['Descripcion']
# Register your models here.

