from django.db import models

# Create your models here.
class Productos(models.Model):    
    name = models.CharField(max_length=255, verbose_name='Nombre')
    brand = models.CharField(max_length=50, verbose_name='Marca')
    price = models.CharField(max_length=50, verbose_name='Precio')
    expiration = models.CharField(max_length=4, verbose_name='Fecha de caducidad')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'


class Clientes(models.Model):    
    name = models.CharField(max_length=255, verbose_name='Nombre')
    last_name = models.CharField(max_length=255, verbose_name='Apellidos')
    address = models.CharField(max_length=255, verbose_name='Dirección')
    email = models.EmailField(max_length=50, verbose_name='E-mail')
    phone = models.CharField(max_length=50, verbose_name='Teléfono')
    country = models.CharField(max_length=50, verbose_name='País')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'


class Proveedores(models.Model):
    productos_id = models.ForeignKey(Productos, on_delete = models.CASCADE, verbose_name='Producto')
    name = models.CharField(max_length=255, verbose_name='Proveedores')
    address = models.CharField(max_length=255, verbose_name='Dirección')
    email = models.EmailField(max_length=50, verbose_name='E-mail')
    phone = models.CharField(max_length=50, verbose_name='Teléfono')
    country = models.CharField(max_length=50, verbose_name='País')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'


class Ventas(models.Model):
    clientes_id = models.ForeignKey(Clientes, on_delete = models.CASCADE, verbose_name='Cliente')
    product = models.CharField(max_length=255, verbose_name='Producto')
    price = models.CharField(max_length=10, verbose_name='Precio')
    state = models.CharField(max_length=50, verbose_name='Estado')
    address = models.CharField(max_length=100, verbose_name='Dirección de envío')

    def __str__(self):
        return self.state

    class Meta:
        verbose_name='Venta'
        verbose_name_plural='Ventas'


class Existencias(models.Model):
    productos_id = models.ForeignKey(Productos, on_delete=models.CASCADE, verbose_name='Producto')
    product = models.CharField(max_length=255, verbose_name='Producto')
    quantity = models.IntegerField(verbose_name='Cantidad')
    product = models.CharField(max_length=255, verbose_name='Producto')
    brand = models.CharField(max_length=100, verbose_name='Marca')
    entry = models.CharField(max_length=4, verbose_name='Fecha de ingreso')
    
    def __str__(self):
        return self.quantity
    
    class Meta:
        verbose_name='Existencia'
        verbose_name_plural='Existencias'