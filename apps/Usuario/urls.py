from django.urls import path
from django.urls.resolvers import URLPattern

from .views import RegistroUsuario, ListarUsuarios
from . import views

# Decorators
from django.contrib.auth.views import login_required

urlpatterns = [
    
    path('registrar/', RegistroUsuario.as_view(), name='usuario_form'),
    path('listar/', login_required(ListarUsuarios.as_view()), name='listar_usuarios'),
]