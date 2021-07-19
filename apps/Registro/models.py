from django.db import models
from django import forms
from django.db.models.fields import IntegerField
# Create your models here.

nombre_pedido = (
    ('Chop suey', 'Chop suey'),
    ('Pollo frito y papas fritas', 'Pollo frito y papas fritas'),
    ('Ensalada BBQ con Pork belly', 'Ensalada BBQ con Pork belly'),
    ('Torta de piña', 'Torta de piña'),
    ('Torta de merengue de mango', 'Torta de merengue de mango'),
    ('Jugo de mango', 'Jugo de mango'),
)


class Pedido(models.Model):

    nombre_plato = models.CharField(choices=nombre_pedido, max_length=100)

    precio = models.IntegerField()

    def __str__(self):

        return self.nombre_plato


class Cliente(models.Model):

    email = models.EmailField(null=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    pedido = models.ForeignKey(
        Pedido, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
