from django.contrib import admin

from Apps.Catalogo.Dato.models import Dato


@admin.register(Dato)

# Register your models here.


class Datoadmin(admin.ModelAdmin):
    list_display = ['Codigo','Nombres','Apellido1','Apellido2','Direccion','Telefono']
    search_fields = ['Codigo']

# Register your models here.
