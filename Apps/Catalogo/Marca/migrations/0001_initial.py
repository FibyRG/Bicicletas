# Generated by Django 4.2.16 on 2024-11-14 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoMarca', models.CharField(max_length=50, unique=True, verbose_name='Codigo')),
                ('DescripcionMarca', models.CharField(max_length=50, verbose_name='Codigo')),
            ],
            options={
                'verbose_name_plural': 'Marcas',
            },
        ),
    ]
