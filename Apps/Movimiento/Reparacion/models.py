from django.db import models
from Apps.Catalogo.Bicicleta.models import Bicicleta
# Create your models here.

class Reparacion(models.Model):
    CodigoReparacion = models.CharField(verbose_name="Codigo", max_length=50, unique=True)
    DescripcionReparacion = models.CharField(verbose_name="Codigo", max_length=50)
    Costo = models.CharField(verbose_name="Codigo", max_length=5)

    class Meta:
        verbose_name_plural = 'Reparaciones'

    def __str__(self):
        return f"´{self.CodigoReparacion} - {self.DescripcionReparacion} - {self.Costo} "


class DetalleReparacion(models.Model):
    BicicletaId = models.ForeignKey(Bicicleta,verbose_name="Bicicleta",on_delete=models.RESTRICT)
    ReparacionId = models.ForeignKey(Reparacion,verbose_name="Reparacion",on_delete=models.RESTRICT)
    FechaReparacion = models.CharField(max_length=10)
    CostoReparacion = models.CharField(max_length=5)
    Observaciones = models.CharField(max_length=50)


def __str__(self):
    return (
        f"{self.BicicletaId} - {self.ReparacionId} - {self.FechaReparacion} - {self.CostoReparacion} - {self.Observaciones} ")
