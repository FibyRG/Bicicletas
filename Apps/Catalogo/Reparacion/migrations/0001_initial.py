# Generated by Django 4.2.16 on 2024-09-25 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoReparacion', models.CharField(max_length=50, unique=True, verbose_name='Codigo')),
                ('DescripcionReparacion', models.CharField(max_length=200)),
                ('Costo', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Reparaciones',
            },
        ),
    ]
