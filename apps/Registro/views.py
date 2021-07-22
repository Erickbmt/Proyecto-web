# django shortcuts
from django.shortcuts import get_object_or_404, redirect, render

# Import clases generics
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Redirect
from django.urls import reverse_lazy
from rest_framework import response

# Imports de modelo y formularios
from .models import *
from .forms import *

# Importaciones de la api
from rest_framework import generics
from .serializers import ClienteSerializer
from  django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Conversiones a json

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

# TOKEN
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings



# Create your views here.




# Cliente VIEWS
# ______________________________ CRUD  ________________________________
# Primero tenemos que registrar los platos
# En pedido_form = pedidoCreate
"""Views donde se impartira el CRUD con la informacion completa de los pedidos"""
def cliente_form(request):

    if request.method == "POST":
        form = ClienteForm(request.POST)
        
        
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            
            return redirect("/confirmacion")
            
    else:
        form = ClienteForm()
        return render(request, 'Registro/cliente_form.html', {'form': form})

# Esta formara parte de cliente ya que con cliente hacemos el pedido
def editar_pedido(request, id):

    instancia = Cliente.objects.get(id=id)

    form = ClienteForm(instance=instancia)

    if request.method == "POST":

        form = ClienteForm(request.POST, instance=instancia)

        if form.is_valid():

            instancia = form.save(commit=False)
            instancia.save()
            
            return redirect("listar_pedido")

    return render(request, "Registro/editar_pedido.html", {'form': form})

# Esta formara parte de cliente ya que con cliente hacemos el pedido
def listar_pedido(request):

    cliente = Cliente.objects.all()
    

    return render(request, 'Registro/listar_pedido.html', {'cliente': cliente})

# Esta formara parte de cliente ya que con cliente hacemos el pedido
def delete_pedido(request, id):

    instancia = get_object_or_404(Cliente, id=id)
    instancia.delete()
    return redirect('listar_pedido')

# Clases genericas para Pedido: solamente para generar un pedido

class pedidoCreate(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'Registro/pedido_form.html'
    success_url = reverse_lazy("confirmacion")

    
    
# ------------------------------------ API  -------------------------------------
# Listar y Crear
@api_view(['GET', 'POST'])
def cliente_collection(request):
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)
    # Agregamos el POST
    elif request.method == 'POST':
        
        serializer= ClienteSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            #Devolvemos una respuesta de codigo 201 si es creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Aqui devolvemos si el proceso falla un 400 que es un Bad request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cliente_element(request, pk):
    # Usaremos get_object_or_404 para mandarnos una 404
    cliente = get_object_or_404(Cliente, id=pk)
    # GET
    if request.method == 'GET':
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    # Eliminar y Editar
    # UPDATE
    elif request.method == 'PUT':
        cliente_new= JSONParser().parse(request)
        serializer= ClienteSerializer(cliente, data=cliente_new)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    elif request.method == 'DELETE':
        
        cliente.delete()
        # Respuesta sin contenido
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# ------------------------- TOKEN -------------------------------------
# Funciona con postman
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# A futuro: intentar obtener por medio de un modelo y una funcion con views.py
# Intentar obtener el token y enviarlo como string el token a la url (<string:token> , Funciona?)
