from collections import namedtuple
from django.urls import path, include
from django.urls.resolvers import URLPattern

from . import views

# Decorators
from django.contrib.auth.views import login_required

urlpatterns = [
    
    # URL CLIENTE FORM
    
    path('cliente_form', views.cliente_form, name='pedido_form'),
    
    # CLIENTE JUNTO CON SUS PEDIDOS
    path('listar_pedido/', login_required(views.listar_pedido), name="listar_pedido"),

    path('editar_pedido/<int:id>', login_required(views.editar_pedido), name="editar_pedido"),
    
    path('delete_pedido/<int:id>/', login_required(views.delete_pedido), name="delete_pedido"),
    # URL PEDIDO: PARA CREAR UN PEDIDO
    path('pedidoCreate', login_required(views.pedidoCreate.as_view()), name="pedidoCreate"),
]

urlpatterns += [
    # API URL
    # Recordatorio: Trata de no confundir las views otra vez
    path('api/', views.cliente_collection, name="cliente_collection"),
    path('api/<int:pk>/', views.cliente_element, name="cliente_element"),
]