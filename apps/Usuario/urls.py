from django.urls import path, include
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    
    path('login', views.login, name='login'),
    path('usuario_form/', views.usuario_form, name='usuario_form'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios')
]