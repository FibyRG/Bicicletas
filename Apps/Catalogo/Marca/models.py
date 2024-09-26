from django.db import models

# Create your models here.
class Marca(models.Model):
    CodigoMarca = models.CharField(verbose_name="Codigo", max_length=50, unique=True)
    DescripcionMarca = models.CharField(verbose_name="Codigo", max_length=50)

    class Meta:
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return f"´{self.CodigoMarca,} - {self.DescripcionMarca} "
