from apps.Vendedor.models import Vendedor
from django.shortcuts import render

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
    
# La funcion de crear un token por cada usuario registrado en la BD esta en Registro/views.py
