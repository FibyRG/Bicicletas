from django.db import models

# Create your models here.
class Reparacion(models.Model):
    CodigoReparacion = models.CharField(verbose_name="Codigo", max_length=50, unique=True)
    DescripcionReparacion = models.CharField(verbose_name="Codigo", max_length=50)
    Costo = models.CharField(verbose_name="Codigo", max_length=5)

    class Meta:
        verbose_name_plural = 'Reparaciones'

    def __str__(self):
        return f"´{self.CodigoReparacion} - {self.DescripcionReparacion} - {self.Costo} "
