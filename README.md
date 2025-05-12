El programa comienza con un mensaje de bienvenida al sistema

Se abre la función principal y con ella 
la función show_menu():

Esta función nos va a imprimir una lista de opciones las cuales 
van a ser validadas por una serie de if y elif 
para poder invocar cada opción 

La opción 1: 
Nos invoca la función add_product: 
Nos pregunta por el nuevo nombre del producto  y usa la función strip() para quitar espacios 

luego hace una validación para verificar si ese nombre que se ingreso al sistema ya existe y así arrojar un mensaje de error

luego se usa un try para manejar excepciones de valores incorrectos
----
EN caso de que el nombre no exista le va a solicitar al usuario 
precio y cantidad de productos

Se maneja la excepción de Value error para verificar que el usuario ingrese valores apropiados como precio en float y cantidad en int

luego se hace una validación para que ls precios y l cantidad sean positivos 

luego vuelve a la función principal
donde me muestra el menú

si ingresamos a la opción dos 



