from django.contrib import admin

from Apps.Movimiento.DetalleRepuesto.models import DetalleRepuesto


@admin.register(DetalleRepuesto)
# Register your models here.

class DetalleRepuestoAdmin(admin.ModelAdmin):
    list_display = [ 'Repuesto_Id','DetalleReparacion_Id','Costo']
    search_fields = ['Repuesto_Id']

# Register your models here.
