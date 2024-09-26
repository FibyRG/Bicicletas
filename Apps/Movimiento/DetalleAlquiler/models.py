from django.db import models

from Apps.Movimiento.Alquiler.models import Alquiler
from Apps.Movimiento.Bicicleta.admin import Bicicleta


# Create your models here.
class DetalleAlquiler(models.Model):
    Bicicleta_Id = models.ForeignKey(Bicicleta,verbose_name="Bicicleta",on_delete=models.RESTRICT)
    Alquiler_Id = models.ForeignKey(Alquiler,verbose_name="Alquiler",on_delete=models.RESTRICT)
    FechaAlquiler = models.DateTimeField(auto_now_add=True)
    FechaDevolucion = models.DateTimeField(auto_now_add=True)
    FechaRealDevolucion = models.DateTimeField(auto_now_add=True)
    Costo = models.CharField(max_length=5)
    Cantidad = models.DateTimeField(max_length=50)

    def __str__(self):
        return (
            f"{self.Bicicleta_Id} - {self.Alquiler_Id} - {self.FechaAlquiler} - {self.FechaDevolucion} - {self.FechaRealDevolucion} -  {self.Costo}"
            f" - {self.Cantidad} ")
