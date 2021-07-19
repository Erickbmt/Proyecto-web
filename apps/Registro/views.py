from django.shortcuts import get_object_or_404, redirect, render

# Import clases generics

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Redirect

from django.urls import reverse_lazy

# Imports de modelo y formularios
from .models import *
from .forms import *
# Create your views here.

# Cliente VIEWS
"""Views donde se impartira el CRUD con la informacion completa de los pedidos"""
def cliente_form(request):

    if request.method == "POST":
        form = ClienteForm(request.POST)
        
        
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            
            return redirect("/confirmacion")
            
    else:
        form = ClienteForm()
        return render(request, 'Registro/cliente_form.html', {'form': form})

# Esta formara parte de cliente ya que con cliente hacemos el pedido
def editar_pedido(request, id):

    instancia = Cliente.objects.get(id=id)

    form = ClienteForm(instance=instancia)

    if request.method == "POST":

        form = ClienteForm(request.POST, instance=instancia)

        if form.is_valid():

            instancia = form.save(commit=False)
            instancia.save()
            
            return redirect("listar_pedido")

    return render(request, "Registro/editar_pedido.html", {'form': form})

# Esta formara parte de cliente ya que con cliente hacemos el pedido
def listar_pedido(request):

    cliente = Cliente.objects.all()
    

    return render(request, 'Registro/listar_pedido.html', {'cliente': cliente})

# Esta formara parte de cliente ya que con cliente hacemos el pedido
def delete_pedido(request, id):

    instancia = get_object_or_404(Cliente, id=id)
    instancia.delete()
    return redirect('listar_pedido')




# Clases genericas para Pedido: solamente para generar un pedido

class pedidoCreate(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'Registro/pedido_form.html'
    success_url = reverse_lazy("confirmacion")


# class pedidoList(ListView):
#     model = Pedido
#     template_name = 'Registro/listar_pedidos.html'
#     # paginate_by = 4


# class pedidoUpdate(UpdateView):
#     model = Pedido
#     form_class = PedidoForm
#     template_name = 'Registro/pedido_form.html'
#     success_url = reverse_lazy('listar_Pedidos')


# class pedidoDelete(DeleteView):
#     model = Pedido
#     template_name = 'Registro/pedido_delete.html'
#     success_url = reverse_lazy('listar_Pedidos')


# # Creare un formulario rapido con las genCliente
# class clienteCreate(CreateView):
#     model = Cliente
#     form_class = ClienteForm
#     template_name = 'Registro/cliente_form.html'
#     success_url = reverse_lazy("confirmacion")