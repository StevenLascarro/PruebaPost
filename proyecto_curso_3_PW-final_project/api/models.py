from django.db import models

# Create your models here.
class Carro(models.Model):
    """
    Modelo que representa la estructura de datos de un 
    registro correspondiente a un carro en base de datos
    """
    modelo = models.IntegerField()
    marca = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_created=True)
    valor = models.BigIntegerField()
