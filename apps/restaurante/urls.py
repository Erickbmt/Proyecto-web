from django.urls import path, include
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('confirmacion/', views.confirmacion, name='confirmacion')
]