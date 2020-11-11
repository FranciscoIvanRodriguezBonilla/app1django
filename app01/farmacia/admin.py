from django.contrib import admin
from .models import Productos, Clientes, Proveedores, Ventas, Existencias
# Register your models here.

admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(Proveedores)
admin.site.register(Ventas)
admin.site.register(Existencias)