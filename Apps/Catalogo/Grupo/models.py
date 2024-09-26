from django.db import models

# Create your models here.
class Grupo(models.Model):
    CodigoGrupo = models.CharField(verbose_name="Codigo", max_length=50, unique=True)
    DescripcionGrupo = models.CharField(verbose_name="Codigo", max_length=50)

    class Meta:
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return f"´{self.CodigoGrupo,} - {self.DescripcionGrupo} "
