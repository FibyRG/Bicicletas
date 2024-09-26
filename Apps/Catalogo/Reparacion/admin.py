from django.contrib import admin

from Apps.Catalogo.Reparacion.models import Reparacion


@admin.register(Reparacion)
# Register your models here.

class ReparacionAdmin(admin.ModelAdmin):
    list_display = ['CodigoReparacion', 'DescripcionReparacion','Costo']
    search_fields = ['CodigoReparacion']

