from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Pedido, Cliente


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido

        fields = ['nombre_plato', 'precio']

        labels = {

            'nombre_plato': 'Plato',
            'precio': 'Precio',

        }

        widgets = {

            'nombre_plato': forms.TextInput(attrs={'class': 'form-control'}),
            # Readonly para que solo muestre el precio
            'precio': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        nombre_pedido = (
            ('Chop suey', 'Chop suey'),
            ('Pollo frito y papas fritas', 'Pollo frito y papas fritas'),
            ('Ensalada BBQ con Pork belly', 'Ensalada BBQ con Pork belly'),
            ('Torta de piña', 'Torta de piña'),
            ('Torta de merengue de mango', 'Torta de merengue de mango'),
            ('Jugo de mango', 'Jugo de mango'),
        )

        fields = ['email', 'direccion', 'telefono', 'nombre', 'pedido']

        labels = {

            'email': 'Correo electronico',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'nombre': 'Nombre Completo',
            'pedido': 'Plato',

        }
        widgets = {

            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pedido': forms.Select(choices="nombre_pedido", attrs={'class': 'form-control'} ),

        }
