from django.contrib import admin

from Apps.Movimiento.DetalleAlquiler.models import DetalleAlquiler


@admin.register(DetalleAlquiler)
# Register your models here.

class DetalleAlquilerAdmin(admin.ModelAdmin):
    list_display = [ 'Bicicleta_Id','Alquiler_Id','FechaAlquiler','FechaDevolucion','FechaRealDevolucion',
                     'Costo','Cantidad']
    search_fields = ['Bicicleta_Id']
# Register your models here.
