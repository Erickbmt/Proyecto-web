from django.urls import path, include
from django.urls.resolvers import URLPattern

from . import views

# Decorators
from django.contrib.auth.views import login_required

urlpatterns = [
    
    # Dejaremos inutilizable por ahora estas url
    
    path('cliente_form', views.cliente_form, name='pedido_form'),
    
    path('listar_pedido/', login_required(views.listar_pedido), name="listar_pedido"),

    path('editar_pedido/<int:id>', login_required(views.editar_pedido), name="editar_pedido"),
    
    path('delete_pedido/<int:id>/', login_required(views.delete_pedido), name="delete_pedido"),
    # URL CLIENTE
    
    path('pedidoCreate', login_required(views.pedidoCreate.as_view()), name="pedidoCreate"),
    
    # Llamando a las clases genericas, que quedaran sin uso por ahora
    
    # path('add_pedido', views.pedidoCreate.as_view(), name="add_pedido"),

    # path('list_pedidos/', views.pedidoList.as_view(), name='list_pedidos'),

    # path('edit_pedido/<int:pk>', views.pedidoUpdate.as_view(), name='edit_pedido'),

    # path('del_pedido/<int:pk>', views.pedidoDelete.as_view(), name='del_pedido'),
]