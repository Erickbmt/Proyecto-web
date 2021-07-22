from collections import namedtuple
from django.urls import path, include
from django.urls.resolvers import URLPattern
from django.contrib.auth.decorators import login_required

from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    # URL CLIENTE FORM
    
    path('vendedor_form', login_required(views.VendedorCreate.as_view()), name='vendedor_form'),
    
    # CLIENTE JUNTO CON SUS PEDIDOS
    path('listar_vendedor/', login_required(views.VendedorList.as_view()), name="listar_vendedor"),

    path('editar_vendedor/<int:pk>', login_required(views.VendedorUpdate.as_view()), name="editar_vendedor"),
    
    path('delete_vendedor/<int:pk>/', login_required(views.VendedorDelete.as_view()), name="delete_vendedor"),
]

urlpatterns += [
    # API URL
    # Recordatorio: Trata de no confundir las views otra vez
    path('api/', views.API_objects.as_view(), name="vendedor_collection"),
    # Es la que se va a guiar por la PK
    path('api/<int:pk>/', views.API_objects_details.as_view(), name="vendedor_element"),
    # Prueba de
    
]

urlpatterns = format_suffix_patterns(urlpatterns)