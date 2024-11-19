from django.contrib import admin

from Apps.Catalogo.Cliente.models import Cliente

@admin.register(Cliente)
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['CodigoCliente', 'Dato_Id']
    search_fields = ['CodigoCliente']
