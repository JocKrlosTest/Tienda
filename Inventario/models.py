from django.db import models
import uuid

from Usuarios.models import Usuario

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.PositiveSmallIntegerField()
    img = models.ImageField(upload_to="productos")
    cantidad = models.PositiveIntegerField()

class Venta(models.Model):
    id = models.UUIDField(auto_created=True,default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ID',editable=False)
    comprador = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField()
    importe = models.PositiveSmallIntegerField()
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_producto} {self.comprador}"    

class Queja(models.Model):
    usuario = models.CharField(max_length=120)
    asunto = models.CharField(max_length=120)
    queja = models.TextField()
    fecha = models.DateTimeField(auto_now=True)

