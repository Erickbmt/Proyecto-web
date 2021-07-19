$(document).ready(function () {
    $(function () {
        $("#submit-form").click(function (event) {
            event.preventDefault();

            var nombre = $("#id_txtNombre").val();
            var correo = $("#id_txtEmail").val();
            var pedido = $("#pedido :selected").text();
            var seleccion = $("#pedido").val();
            var precio = $(0);
            

            // Estos if y else if sirven para ponerle el precio segun la opcion elegida en el select
            // Ya que en la variable que hemos creado (seleccion) le asignamos el value de las opciones del select
            
            if (seleccion == "1"){

                precio = 4500;
            }
            else if (seleccion == "2"){

                precio = 2000;
            }

            else if (seleccion == "3"){

                precio = 2500;
            }

            else if (seleccion == "4"){

                precio = 1200;
            }

            else if (seleccion == "5"){

                precio = 1800;
            }
            
            var fila = '<tr><th>' + nombre + '</th><th>' + correo + '</th><th>' + pedido + '</th><th>'+ '$' + precio + '</th></tr>';

            $('#tabla_pedidos>tbody').append(fila);

        });
    });



});