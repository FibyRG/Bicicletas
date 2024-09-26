from django.db import models

# Create your models here.
class Dato(models.Model):
    Codigo = models.CharField(verbose_name="Codigo", max_length=50, unique=True)
    Nombres = models.CharField(verbose_name="Nombre",max_length=50)
    Apellido1 = models.CharField(verbose_name="Apellido1",max_length=20)
    Apellido2 = models.CharField(verbose_name="Apellido2",max_length=20)
    Direccion = models.CharField(verbose_name="Direccion",max_length=100)
    Telefono = models.CharField(verbose_name="Telefono",max_length=50)

    class Meta:
        verbose_name_plural = 'Datos'
    def __str__(self):
        return f"´{self.Codigo,} - {self.Nombres} - {self.Apellido1} - {self.Apellido2} - {self.Direccion} - {self.Telefono}"
