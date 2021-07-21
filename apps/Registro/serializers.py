from rest_framework import serializers

from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        # En el field de pedido tiene que poner un ID del plato al cual se refiere
        # Hay hasta 6 platos: 6 id's
        fields = ('id', 'nombre', 'email', 'direccion', 'telefono', 'pedido')