from django.db import models

# Create your models here.
class Repuesto(models.Model):
    CodigoRepuesto = models.CharField(verbose_name="Codigo", max_length=50, unique=True)
    DescripcionRepuesto = models.CharField(verbose_name="Codigo", max_length=50)
    Costo = models.CharField(verbose_name="Codigo", max_length=50)


class Meta:
    verbose_name_plural = 'Repuestos'


def __str__(self):
    return f"´{self.CodigoRepuesto} - {self.DescripcionRepuesto} - {self.Costo} "
