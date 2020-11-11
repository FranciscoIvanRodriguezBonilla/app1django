# Generated by Django 3.1.2 on 2020-10-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0003_existencias_proveedores_ventas'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='price',
            field=models.FloatField(default=0, max_length=100, verbose_name='Precio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventas',
            name='product',
            field=models.CharField(default=0, max_length=255, verbose_name='Producto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='existencias',
            name='quantity',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
    ]
