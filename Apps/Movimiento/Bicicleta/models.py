from django.db import models

from Apps.Catalogo.Grupo.models import Grupo
from Apps.Catalogo.Marca.models import Marca


# Create your models here.
class Bicicleta(models.Model):
    CodigoDeBicicleta = models.CharField(verbose_name="CodigoDeBicicleta",max_length=8)
    DescripcionBicicleta = models.CharField(verbose_name="DescripcionBicicleta",max_length=50)
    Grupo_Id = models.ForeignKey(Grupo,verbose_name="Grupo",on_delete=models.RESTRICT)
    Marca_Id = models.ForeignKey(Marca,verbose_name="Marca",on_delete=models.RESTRICT)
    AnioIngreso = models.CharField(max_length=10)
    PrecioCompra = models.CharField(max_length=5)
    Devaluacion = models.CharField(max_length=50)
    CostoAlquiler = models.CharField(max_length=5)

    def __str__(self):
        return (
            f"{self.CodigoDeBicicleta} - {self.DescripcionBicicleta} - {self.Grupo_Id} - {self.Marca_Id} - {self.AnioIngreso}"
            f" - {self.PrecioCompra} - {self.Devaluacion} - {self.CostoAlquiler}")