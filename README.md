# PROYECTO SPRINT 8 - JULIÁN SOTELO - GRUPO 36
# AUTOMATIZACIÓN PRUEBAS DE FUNCIONALIDAD EN APP URBAN ROUTES 🚕 
 
# 📚Técnicas - Tecnologías utilizadas:

- Python.
- Selenium.
- Localizadores XPath.
- DOM.

# 📃 Creación de archivos:

🔵 "_data.py_"; en este archivo se almacena la URL para interactuar con la APP.

1. urban_routes_url: se copia el link del servidor entre "".
2. address_from: dirección de salida predeterminada.
3. address_to: dirección de llegada predeterminada.
4. phone_number: número de teléfono predeterminado.
5. card_number, card_code: datos de la tarjeta predeterminados.
6. message_for_driver: mensaje para el conductor.

🟢 "_helpers.py_"; en este archivo se almacena la función que recibe el código de confirmación al ingresar un número de teléfono.

🟡 "_locators.py_"; en este archivo se almacenan todos los localizadores de botones y cajas de texto que se utilizan en cada función.

🔴 "_main.py_"; en este archivo se almacenan:

1. Métodos que se utilizaran para cada función.
3. La prueba de funcionalidad para pedir un taxi en la tarifa Comfort.

# 📝 Ejecución de pruebas:

Las pruebas de funcionalidad para el proceso de pedir un taxi se desarrollan en el siguiente orden:

1. Introducir direcciones de salida y llegada.
2. Seleccionar la tarifa "Comfort".
3. Registrar el número de teléfono.
4. Ingresar una tarjeta de crédito.
5. Escribir un mensaje para el conductor.
6. Pedir una manta y pañuelos.
7. Pedir 2 helados.
8. Confirmar el pedido del taxi.

El resultado final al confirmar el pedido del taxi será una ventana donde inicia un temporizador de 30 segundos, obteniendo al final los datos del conductor y el carro pedidos.

En el siguiente video se puede ver un demo de las pruebas ejecutadas en Urban Routes:

[![Ver video](https://img.icons8.com/ios-filled/100/000000/play-button-circled.png)](https://drive.google.com/file/d/1AFXqvXJTvih6xzhRmygF5S3dvFVcWmTq/view?usp=drive_link)



