from django.db import models

from  Apps.Catalogo.Dato.models import Dato

# Create your models here.
class Empleado(models.Model):
    Dato_Id = models.ForeignKey(Dato,verbose_name="Dato", max_length=50, on_delete=models.PROTECT)
    Salario = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Salario")


def __str__(self):
    return f"{self.Dato_Id} - {self.Salario}"
