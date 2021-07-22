from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Vendedor


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor

        fields = ['rut', 'nombre', 'email', 'telefono', 'sueldo', 'nivel_estudio']

        labels = {

            'rut': 'Rut',
            'nombre': 'Nombre Completo',
            'email': 'Correo electronico',
            'telefono': 'Telefono',
            'sueldo': 'Salario',
            'nivel_estudio': 'Nivel de estudio',

        }

        widgets = {

            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'sueldo': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel_estudio': forms.Select(choices= "NIVELES_ESTUDIOS",attrs={'class': 'form-control'}),

        }