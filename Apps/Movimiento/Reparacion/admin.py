from django.contrib import admin

from Apps.Movimiento.Reparacion.models import Reparacion, DetalleReparacion


@admin.register(Reparacion)
# Register your models here.

class ReparacionAdmin(admin.ModelAdmin):
    list_display = [ 'CodigoReparacion','DescripcionReparacion','Costo']
    search_fields = ['CodigoReparacion']

@admin.register(DetalleReparacion)
class DetalleReparacionAdmin(admin.ModelAdmin):
        list_display = ['BicicletaId', 'ReparacionId', 'FechaReparacion', 'CostoReparacion',
                        'Observaciones']
        search_fields = ['BicicletaId']

