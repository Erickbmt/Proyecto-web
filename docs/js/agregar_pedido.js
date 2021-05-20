$(document).ready(function () {
    $(function () {
        $("#submit-form").click(function (event) {
            event.preventDefault();

            var nombre = $("#id_txtNombre").val();
            var correo = $("#id_txtEmail").val();
            var pedido = $("#pedidoSeleccionado").val();
            var fila = '<tr><th>' + nombre + '</th><th>' + correo + '</th><th>' + pedido + '</th></tr>';

            $('#tabla_pedidos>tbody').append(fila);

        });
    });



});