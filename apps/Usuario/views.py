from django.shortcuts import render

# Create your views here.



def login(request):
    
    return render(request, 'Usuario/login.html')

def usuario_form(request):
    
    return render(request, 'Usuario/usuario_form.html')


def listar_usuarios(request):
    
    
    return render(request, 'Usuario/listar_usuarios.html')