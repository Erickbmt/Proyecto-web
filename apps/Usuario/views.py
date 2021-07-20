from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView

# importamos user

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# importar formulario

from .form import RegistroForm
# Create your views here.



class RegistroUsuario(CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'Usuario/usuario_form.html'
    success_url = reverse_lazy("confirmacion")

class ListarUsuarios(ListView):
    model = User
    template_name = 'Usuario/listar_usuarios.html'