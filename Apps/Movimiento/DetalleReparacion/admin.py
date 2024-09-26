from django.contrib import admin

from Apps.Movimiento.DetalleReparacion.models import DetalleReparacion


@admin.register(DetalleReparacion)
# Register your models here.

class DetalleReparacionAdmin(admin.ModelAdmin):
    list_display = [ 'BicicletaId','ReparacionId','FechaReparacion','CostoReparacion',
                     'Observaciones']
    search_fields = ['BicicletaId']
# Register your models here.
