# Generated by Django 4.2.16 on 2024-09-26 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Alquiler', '0001_initial'),
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='Cliente_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Cliente.cliente', verbose_name='Cliente'),
        ),
    ]
