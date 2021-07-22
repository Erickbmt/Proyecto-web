from apps.Vendedor.models import Vendedor
from django.shortcuts import get_object_or_404, redirect, render

# Import clases generics
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Redirect 

from django.urls import reverse_lazy

# Importar forms

from .forms import VendedorForm


# Importar serializer y rest_framework generics
from .serializers import VendedorSerializer
# las importaciones para la API 
from rest_framework import generics
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

# ------------------------- CRUD CON GENERICS ----------------------------

class VendedorList (ListView):                    
    model = Vendedor
    template_name = 'Vendedor/listar_vendedor.html'

class VendedorCreate (CreateView):
    model = Vendedor
    form_class = VendedorForm
    template_name = 'Vendedor/vendedor_form.html'
    success_url = reverse_lazy('listar_vendedor')

class VendedorUpdate(UpdateView):
    model = Vendedor
    form_class = VendedorForm
    template_name = 'Vendedor/editar_vendedor.html'
    success_url = reverse_lazy('listar_vendedor')

class VendedorDelete(DeleteView):
    model = Vendedor
    template_name = 'Vendedor/delete_vendedor.html'
    success_url = reverse_lazy('listar_vendedor')


# ---------------- API CON GENERICS ---------------------------
class API_objects(generics.ListCreateAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    

# Aqui abajo se encuentra si se prefiere sin clases generics

# @api_view(['GET', 'POST'])
# def vendedor_collection(request):
#     if request.method == 'GET':
#         vendedor = Vendedor.objects.all()
#         serializer = VendedorSerializer(vendedor, many=True)
#         return Response(serializer.data)
#     # Agregamos el POST
#     elif request.method == 'POST':
        
#         serializer= VendedorSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             #Devolvemos una respuesta de codigo 201 si es creado
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # Aqui devolvemos si el proceso falla un 400 que es un Bad request
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def vendedor_element(request, pk):
#     # Usaremos get_object_or_404 para mandarnos una 404
#     vendedor = get_object_or_404(Vendedor, id=pk)
#     # GET
#     if request.method == 'GET':
#         serializer = VendedorSerializer(vendedor)
#         return Response(serializer.data)
#     # Eliminar y Editar
#     # UPDATE
#     elif request.method == 'PUT':
#         vendedor_new= JSONParser().parse(request)
#         serializer= VendedorSerializer(vendedor, data=vendedor_new)
        
#         if serializer.is_valid():
            
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
#     # DELETE
#     elif request.method == 'DELETE':
        
#         vendedor.delete()
#         # Respuesta sin contenido
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# La funcion de crear un token por cada usuario registrado en la BD esta en Registro/views.py
