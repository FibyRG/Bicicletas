from django.db import models


from Apps.Catalogo.Cliente.models import Cliente
from Apps.Catalogo.Empleado.models import Empleado
from Apps.Catalogo.Bicicleta.models import Bicicleta


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

class DetalleAlquiler(models.Model):
    Bicicleta_Id = models.ForeignKey(Bicicleta,verbose_name="Bicicleta",on_delete=models.RESTRICT)
    Alquiler_Id = models.ForeignKey(Alquiler,verbose_name="Alquiler",on_delete=models.RESTRICT , related_name='DetallesAlquiler')
    FechaAlquiler = models.DateTimeField(auto_now_add=True)
    FechaDevolucion = models.DateTimeField()
    FechaRealDevolucion = models.DateTimeField(null=True, blank=True)
    Costo = models.CharField(max_length=5)
    Cantidad = models.IntegerField()

    def __str__(self):
        return (
            f"{self.Bicicleta_Id} - {self.Alquiler_Id} - {self.FechaAlquiler} - {self.FechaDevolucion} - {self.FechaRealDevolucion} -  {self.Costo}"
            f" - {self.Cantidad} ")
