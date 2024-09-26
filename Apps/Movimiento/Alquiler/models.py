from django.db import models


from Apps.Movimiento.Cliente.models import Cliente
from Apps.Movimiento.Empleado.models import Empleado


# Create your models here.
class Alquiler(models.Model):
    FechaAlquiler = models.DateTimeField(verbose_name="FechaAlquiler",auto_now_add=True)
    Descripcion = models.CharField(verbose_name="Descripcion",max_length=50)
    CodigoAlquiler = models.CharField(verbose_name="CodigoAlquiler",max_length=8)
    Cliente_Id = models.ForeignKey(Cliente,verbose_name="Cliente",on_delete=models.RESTRICT)
    Empleado_Id = models.ForeignKey(Empleado,verbose_name="Empleado",on_delete=models.RESTRICT)

    def __str__(self):
        return (f"{self.FechaAlquiler} - {self.Descripcion} - {self.CodigoAlquiler} - {self.Cliente_Id} - {self.Empleado_Id}"
                f" - {self.Empleado_Id}")