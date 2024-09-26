from django.db import models

from Apps.Catalogo.Repuesto.models import Repuesto
from Apps.Movimiento.DetalleReparacion.models import DetalleReparacion


# Create your models here.
class DetalleRepuesto(models.Model):
    Repuesto_Id = models.ForeignKey(Repuesto,on_delete=models.RESTRICT)
    DetalleReparacion_Id = models.ForeignKey(DetalleReparacion,on_delete=models.RESTRICT)
    Costo = models.CharField(max_length=5)

def __str__(self):
    return (
        f"{self.Repuesto_Id} - {self.DetalleReparacion_Id} - {self.Costo}  ")

