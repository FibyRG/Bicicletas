from django.contrib import admin

from Apps.Catalogo.Repuesto.models import Repuesto


@admin.register(Repuesto)
# Register your models here.

class RepuestoAdmin(admin.ModelAdmin):
    list_display = ['CodigoRepuesto', 'DescripcionRepuesto','Costo']
    search_fields = ['CodigoRepuesto']

