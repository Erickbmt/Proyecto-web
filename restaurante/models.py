from django.db import models
from django.db.models.fields import EmailField, TextField

# Create your models here.


class Cliente(models.Model):

    email = models.EmailField()
    direccion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.nombre
    

class Pedido(models.Model):
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    
    
    def __str__(self):
        return self.nombre
