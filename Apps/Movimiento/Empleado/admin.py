from django.contrib import admin
from Apps.Movimiento.Empleado.models import Empleado

@admin.register(Empleado)
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = [ 'Dato_Id','Salario']
    search_fields = ['Dato_Id']
# Register your models here.
