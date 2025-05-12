"""
Este programa permite agregar, consultar, actualizar y eliminar productos
y calcular el valor total del inventario.
"""

# Función para agregar productos al inventario
def add_product(inventory):
    """Añade un producto nuevo si no existe y valida entradas."""
    name = input("Nombre del producto: ").strip()  # Solicita nombre y elimina espacios extras

    # Verifica si el producto ya existe (ignora mayúsculas/minúsculas)
    if any(p['name'].lower() == name.lower() for p in inventory):
        print(f" El producto '{name}' ya existe en el inventario.")
        return

    try:
        # Solicita y convierte el precio y la cantidad
        price = float(input("Precio unitario: "))
        quantity = int(input("Cantidad disponible: "))
    except ValueError:
        # Si hay error en la conversión, lo indica
        print("Entrada inválida. Precio y cantidad deben ser números.")
        return

    # Agrega el producto al inventario como diccionario
    inventory.append({'name': name, 'price': price, 'quantity': quantity})
    print(f"Producto '{name}' añadido con éxito.\n")

# Función para buscar un producto por su nombre
def find_product(inventory, name):
    """Busca un producto por nombre y lo devuelve."""
    for product in inventory:
        if product['name'].lower() == name.lower():  # Comparación sin importar mayúsculas
            return product
    return None  # Si no lo encuentra, retorna None

# Función para consultar un producto específico
def consult_product(inventory):
    """Consulta y muestra los datos de un producto"""
    name = input("Nombre del producto a consultar: ").strip()
    product = find_product(inventory, name)  # Busca el producto

    if product:
        # Si lo encuentra, muestra su información
        print(f"Producto: {product['name']}")
        print(f"Precio: {product['price']}")
        print(f"Cantidad: {product['quantity']}\n")
    else:
        print(f"El producto '{name}' no se encuentra en el inventario.\n")

# Función para actualizar el precio de un producto
def update_price(inventory):
    """Actualiza el precio de un producto"""
    name = input("Nombre del producto a actualizar: ").strip()
    product = find_product(inventory, name)

    if not product:
        print(f"No existe el producto '{name}'.\n")
        return

    try:
        new_price = float(input("Nuevo precio unitario: "))  # Solicita nuevo precio
    except ValueError:
        print("Precio inválido. Debe ser un número.\n")
        return

    product['price'] = new_price  # Actualiza el precio
    print(f"Precio de '{name}' actualizado a {new_price}.\n")

# Función para eliminar un producto
def delete_product(inventory):
    """Elimina un producto"""
    name = input("Nombre del producto a eliminar: ").strip()
    product = find_product(inventory, name)

    if not product:
        print(f" No existe el producto '{name}'.\n")
        return

    inventory.remove(product)  # Elimina el producto del inventario
    print(f"Producto '{name}' eliminado del inventario.\n")

# Función para calcular el valor total del inventario
def calculate_total(inventory):
    """Calcula y muestra el valor total usando una función lambda."""
    # Multiplica precio * cantidad por cada producto y suma todo
    total_value = (lambda inv: sum(p['price'] * p['quantity'] for p in inv))(inventory)
    print(f"Valor total del inventario: {total_value:.2f}\n")  # Muestra con 2 decimales

# Función que muestra el menú de opciones
def show_menu():
    """Muestra el menú de opciones al usuario."""
    print("=== MENÚ DE INVENTARIO ===")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total")
    print("6. Salir")
    print("==========================")

# Función principal que ejecuta el programa
def main():
    """Función principal que controla el flujo del programa."""
    inventory = []  # Lista vacía donde se guardarán los productos

    while True:
        show_menu()  # Muestra el menú
        choice = input("Selecciona una opción: ").strip()  # Pide opción al usuario

        # Según la opción elegida, llama a la función correspondiente
        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            consult_product(inventory)
        elif choice == '3':
            update_price(inventory)
        elif choice == '4':
            delete_product(inventory)
        elif choice == '5':
            calculate_total(inventory)
        elif choice == '6':
            print("__FINN__")  # Mensaje de cierre
            break  # Sale del bucle
        else:
            print("Opcion invalida.\n")  # Maneja opción no válida

# Llamada al main solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
