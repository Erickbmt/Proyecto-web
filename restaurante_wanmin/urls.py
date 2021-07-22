"""restaurante_wanmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from apps import Usuario
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# Login
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

# TOKEN

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.restaurante.urls') ),
    path('usuario/', include('apps.Usuario.urls')),
    path('registro/', include('apps.Registro.urls')),
    
    
    
    # PATH LOGIN 
    
    path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='Usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # Nueva app
    path('vendedor/', include('apps.Vendedor.urls')),
    # TOKEN
    
    path('api-token-auth/', obtain_auth_token, name='api_token_auth' )
]
