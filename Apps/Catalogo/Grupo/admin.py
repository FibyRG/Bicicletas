from django.contrib import admin

from Apps.Catalogo.Grupo.models import Grupo


@admin.register(Grupo)
# Register your models here.

class GrupoAdmin(admin.ModelAdmin):
    list_display = ['CodigoGrupo', 'DescripcionGrupo']
    search_fields = ['CodigoGrupo']

