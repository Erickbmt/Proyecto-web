$("#formulario1").validate({
    rules: {
        "txtEmail": {
            required: true,
            email: true
        },
        "txtDireccion": {
            required: true,
            minlength: 5
        },
        "txtNombre": {
            required: true
            
        },
        "pedido":{

            required: true

        }
    }, // --> Fin de reglas
    messages: {
        "txtEmail": {
            required: 'Ingrese email valido',
            email: 'No cumple formato de ingreso'
        },
        "txtDireccion": {
            required: 'Ingrese direccion valida para el pedido',
            minlength: 'La direcccion tiene que tener un largo de 5 caracteres'
        },
        "txtNombre": {
            required: 'Ingrese su nombre para identificarlo'
        },
        "pedido":{
            if(pedido = pedidoSelelccionado){
                required: 'Por favor seleccione una de las opciones'
            }
        }
    } //-->Fin de mensajes
 
});
