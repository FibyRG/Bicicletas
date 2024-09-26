from django.db import models
"""
Clientes
"""

from Apps.Catalogo.Dato.models import Dato


# Create your models here.
class Cliente(models.Model):
    CodigoCliente = models.CharField(verbose_name="Codigo", max_length=50, unique=True)
    Dato_Id = models.ForeignKey(Dato,verbose_name="Dato_Id", max_length=50, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.CodigoCliente} - {self.Dato_Id}"
