from django import forms
from .models import Pedido



class PedidoForm(forms.ModelForm):
    
    model= Pedido
    
    fields= ("")