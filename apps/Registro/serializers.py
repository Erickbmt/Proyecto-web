from rest_framework import serializers

from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        # En el field de pedido tiene que poner un ID del plato al cual se refiere
        # Hay hasta 6 platos: 6 id's
        # IGNORE EL MENSAJE DE ARRIBA: Ahora estan los id's 1 ,2 ,3 ,4 ,5 ,6 y 25 en adelante
        # No pregunte como paso, solo disfrute
        fields = ('id', 'nombre', 'email', 'direccion', 'telefono', 'pedido')