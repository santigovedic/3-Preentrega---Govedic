from django.db import models


class Producto(models.Model):

    tipo = models.CharField(max_length=15) # Cola, Agua, Fernet, Cerveza, etc.
    marca = models.CharField(max_length=15) # Branca, Andes, etc.
    stock = models.IntegerField() # Cuanto stock ingresa a la base de datos con la carga.

    def __str__(self):
        return f"Tipo: {self.tipo} | Marca: {self.marca}"


class Cliente(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()


class Proveedor(models.Model):

    razon_social = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
