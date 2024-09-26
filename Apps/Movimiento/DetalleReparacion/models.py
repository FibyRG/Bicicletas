from django.db import models

from Apps.Catalogo.Reparacion.models import Reparacion
from Apps.Movimiento.Bicicleta.admin import Bicicleta


# Create your models here.
class DetalleReparacion(models.Model):
    BicicletaId = models.ForeignKey(Bicicleta,verbose_name="Bicicleta",on_delete=models.RESTRICT)
    ReparacionId = models.ForeignKey(Reparacion,verbose_name="Reparacion",on_delete=models.RESTRICT)
    FechaReparacion = models.CharField(max_length=10)
    CostoReparacion = models.CharField(max_length=5)
    Observaciones = models.CharField(max_length=50)


def __str__(self):
    return (
        f"{self.BicicletaId} - {self.ReparacionId} - {self.FechaReparacion} - {self.CostoReparacion} - {self.Observaciones} ")
