from django.contrib import admin
from Apps.Catalogo.Marca.models import Marca


@admin.register(Marca)
# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
    list_display = ['CodigoMarca', 'DescripcionMarca']
    search_fields = ['CodigoMarca']



