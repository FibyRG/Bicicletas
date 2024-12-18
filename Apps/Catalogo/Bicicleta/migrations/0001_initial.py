# Generated by Django 4.2.16 on 2024-11-14 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Marca', '0001_initial'),
        ('Grupo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bicicleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoDeBicicleta', models.CharField(max_length=8, verbose_name='CodigoDeBicicleta')),
                ('DescripcionBicicleta', models.CharField(max_length=50, verbose_name='DescripcionBicicleta')),
                ('AnioIngreso', models.CharField(max_length=10)),
                ('PrecioCompra', models.CharField(max_length=5)),
                ('Devaluacion', models.CharField(max_length=50)),
                ('CostoAlquiler', models.CharField(max_length=5)),
                ('Grupo_Id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Grupo.grupo', verbose_name='Grupo')),
                ('Marca_Id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Marca.marca', verbose_name='Marca')),
            ],
        ),
    ]
