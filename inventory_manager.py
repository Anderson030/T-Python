
"""
Este programa permite agregar, consultar, actualizar y  eliminar productos
y calcular el valor total del inventario.
"""

def add_product(inventory):
    """Añade un producto nuevo si no existe y valida entradas."""
    name = input("Nombre del producto: ").strip()
    # sensible a may y min
    if any(p['name'].lower() == name.lower() for p in inventory):
        print(f"⚠ El producto '{name}' ya existe en el inventario.")
        return

    try:
        price = float(input("Precio unitario: "))
        quantity = int(input("Cantidad disponible: "))
    except ValueError:
        print("Entrada inválida. Precio y cantidad deben ser números.")
        return

    inventory.append({'name': name, 'price': price, 'quantity': quantity})
    print(f"Producto '{name}' añadido con éxito.\n")

def find_product(inventory, name):
    """Busca un producto por nombre y lo devuelve."""
    for product in inventory:
        if product['name'].lower() == name.lower():
            return product
    return None

def consult_product(inventory):
    """Consulta y muestra los datos de un producto"""
    name = input("Nombre del producto a consultar: ").strip()
    product = find_product(inventory, name)
    if product:
        print(f"Producto: {product['name']}")
        print(f"Precio: {product['price']}")
        print(f"Cantidad: {product['quantity']}\n")
    else:
        print(f"El producto '{name}' no se encuentra en el inventario.\n")

def update_price(inventory):
    """Actualiza el precio de un producto"""
    name = input("Nombre del producto a actualizar: ").strip()
    product = find_product(inventory, name)
    if not product:
        print(f"No existe el producto '{name}'.\n")
        return

    try:
        new_price = float(input("Nuevo precio unitario: "))
    except ValueError:
        print("Precio inválido. Debe ser un número.\n")
        return

    product['price'] = new_price
    print(f"Precio de '{name}' actualizado a {new_price}.\n")

def delete_product(inventory):
    """Elimina un producto"""
    name = input("Nombre del producto a eliminar: ").strip()
    product = find_product(inventory, name)
    if not product:
        print(f" No existe el producto '{name}'.\n")
        return

    inventory.remove(product)
    print(f"Producto '{name}' eliminado del inventario.\n")

def calculate_total(inventory):
    """Calcula y muestra el valor total usando una función lambda."""
    total_value = (lambda inv: sum(p['price'] * p['quantity'] for p in inv))(inventory)
    print(f"Valor total del inventario: {total_value:.2f}\n")

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

def main():
    """Función principal que controla el flujo del programa."""
    inventory = []
    while True:
        show_menu()
        choice = input("Selecciona una opción: ").strip()

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
            print("__FINN__")
            break
        else:
            print("Opcion invalida.\n")

if __name__ == "__main__":
    main()
