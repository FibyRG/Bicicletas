from django.contrib import admin

from Apps.Movimiento.Bicicleta.models import Bicicleta


@admin.register(Bicicleta)
# Register your models here.

class BicicletaAdmin(admin.ModelAdmin):
    list_display = [ 'CodigoDeBicicleta','DescripcionBicicleta','Grupo_Id','Marca_Id','AnioIngreso',
                     'PrecioCompra','Devaluacion','CostoAlquiler']
    search_fields = ['Descripcion']

# Register your models here.
