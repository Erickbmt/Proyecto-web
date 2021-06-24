from django.shortcuts import render
from .models import * 

# Create your views here.


def home(request):
    
    return render(request, 'restaurante/home.html')

def menu(request):
    
    return render(request, 'restaurante/menu.html')

def pedido(request):
    
    pedidos= Pedido.objects.all()
    
    return render(request, 'restaurante/pedido.html', {'pedidos': pedidos})

def confirmacion(request):
    
    return render(request, 'restaurante/pagina_confirmacion.html')



