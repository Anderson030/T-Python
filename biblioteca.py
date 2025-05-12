# Gestor de Catálogo de Libros
# Autor: ChatGPT (según los requisitos del usuario)
# Descripción: Un sistema simple en consola para gestionar un catálogo de libros

from datetime import datetime

# Catálogo inicial con 5 libros de ejemplo
catalogo = [
    {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "genero": "Novela", "anio": 1967, "cantidad": 3, "precio": 25000},
    {"titulo": "1984", "autor": "George Orwell", "genero": "Distopía", "anio": 1949, "cantidad": 5, "precio": 18000},
    {"titulo": "Matar a un Ruiseñor", "autor": "Harper Lee", "genero": "Clásico", "anio": 1960, "cantidad": 4, "precio": 20000},
    {"titulo": "Don Quijote", "autor": "Miguel de Cervantes", "genero": "Clásico", "anio": 1605, "cantidad": 2, "precio": 30000},
    {"titulo": "El Gran Gatsby", "autor": "F. Scott Fitzgerald", "genero": "Clásico", "anio": 1925, "cantidad": 6, "precio": 22000},
]

# Función para registrar un nuevo libro
def registrar_libro():
    titulo = input("Ingrese el título del libro: ").strip()
    autor = input("Ingrese el autor: ").strip()
    genero = input("Ingrese el género: ").strip()

    try:
        anio = int(input("Ingrese el año de publicación: "))
        if anio > datetime.now().year or anio < 1800:
            print("Año inválido. Ingrese un valor entre 1800 y 2024.")
            return
        cantidad = int(input("Ingrese la cantidad disponible: "))
        precio = float(input("Ingrese el precio de reposición: "))
        if cantidad < 0 or precio <= 0:
            print("La cantidad y el precio deben ser positivos.")
            return
    except ValueError:
        print("Entrada inválida. Use números para año, cantidad y precio.")
        return

    catalogo.append({"titulo": titulo, "autor": autor, "genero": genero,
                     "anio": anio, "cantidad": cantidad, "precio": precio})
    print("Libro registrado exitosamente.\n")

# Función para buscar y mostrar un libro por título o autor (sin distinguir mayúsculas)
def buscar_libro():
    consulta = input("Ingrese título o autor a buscar: ").strip().lower()
    encontrado = False
    for libro in catalogo:
        if consulta in libro["titulo"].lower() or consulta in libro["autor"].lower():
            mostrar_libro(libro)
            encontrado = True
    if not encontrado:
        print("Libro no encontrado. ¿Desea registrarlo?")

# Mostrar detalles del libro
def mostrar_libro(libro):
    print("\n--- Detalles del Libro ---")
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
    print(f"Género: {libro['genero']}")
    print(f"Año: {libro['anio']}")
    print(f"Cantidad: {libro['cantidad']}")
    print(f"Precio de Reposición: {libro['precio']}\n")

# Función para actualizar cantidad o precio
def actualizar_libro():
    titulo = input("Ingrese el título del libro a actualizar: ").strip().lower()
    for libro in catalogo:
        if libro["titulo"].lower() == titulo:
            try:
                cantidad = int(input("Ingrese nueva cantidad: "))
                precio = float(input("Ingrese nuevo precio de reposición: "))
                if cantidad < 0 or precio <= 0:
                    print("Los valores deben ser positivos.")
                    return
                libro["cantidad"] = cantidad
                libro["precio"] = precio
                print("Libro actualizado correctamente.\n")
                return
            except ValueError:
                print("Entrada inválida. Use números válidos.")
                return
    print("Libro no encontrado.")

# Función para eliminar un libro con confirmación
def eliminar_libro():
    titulo = input("Ingrese el título del libro a eliminar: ").strip().lower()
    for libro in catalogo:
        if libro["titulo"].lower() == titulo:
            confirmar = input(f"¿Está seguro que desea eliminar '{libro['titulo']}'? (s/n): ")
            if confirmar.lower() == 's':
                catalogo.remove(libro)
                print("Libro eliminado exitosamente.\n")
            else:
                print("Eliminación cancelada.\n")
            return
    print("Libro no encontrado.\n")

# Función para generar reportes
def generar_reportes():
    valor_total = sum(libro['precio'] * libro['cantidad'] for libro in catalogo)
    print(f"\nValor total del inventario: {valor_total:.2f}")

    generos = {}
    for libro in catalogo:
        genero = libro['genero']
        if genero not in generos:
            generos[genero] = []
        generos[genero].append(libro)

    for genero, libros in generos.items():
        antiguo = min(libros, key=lambda l: l['anio'])
        reciente = max(libros, key=lambda l: l['anio'])
        print(f"\nGénero: {genero}")
        print(f"  Más antiguo: {antiguo['titulo']} ({antiguo['anio']})")
        print(f"  Más reciente: {reciente['titulo']} ({reciente['anio']})")

# Interfaz de menú para interacción con el usuario
def menu_principal():
    while True:
        print("\n--- Menú del Catálogo de Libros ---")
        print("1. Registrar nuevo libro")
        print("2. Buscar libro")
        print("3. Actualizar información")
        print("4. Eliminar libro")
        print("5. Generar reportes")
        print("6. Salir")
        opcion = input("Elija una opción: ").strip()

        if opcion == '1':
            registrar_libro()
        elif opcion == '2':
            buscar_libro()
        elif opcion == '3':
            actualizar_libro()
        elif opcion == '4':
            eliminar_libro()
        elif opcion == '5':
            generar_reportes()
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor elija un número del 1 al 6.")

if __name__ == "__main__":
    menu_principal()
