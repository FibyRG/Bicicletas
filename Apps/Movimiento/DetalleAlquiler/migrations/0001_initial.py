# Generated by Django 4.2.16 on 2024-09-26 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Alquiler', '0001_initial'),
        ('Bicicleta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleAlquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaAlquiler', models.DateTimeField(auto_now_add=True)),
                ('FechaDevolucion', models.DateTimeField(auto_now_add=True)),
                ('FechaRealDevolucion', models.DateTimeField(auto_now_add=True)),
                ('Costo', models.CharField(max_length=5)),
                ('Cantidad', models.DateTimeField(max_length=50)),
                ('Alquiler_Id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Alquiler.alquiler', verbose_name='Alquiler')),
                ('Bicicleta_Id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Bicicleta.bicicleta', verbose_name='Bicicleta')),
            ],
        ),
    ]