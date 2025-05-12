# Agenda de Contactos
# Este programa permite gestionar contactos: agregar, buscar, editar, eliminar y mostrar lista ordenada.

contactos = []

# Función para agregar un nuevo contacto
def agregar_contacto():
    nombre = input("Nombre: ").strip()
    numero = input("Número de teléfono: ").strip()
    correo = input("Correo electrónico: ").strip()

    # Verifica si ya existe
    for c in contactos:
        if c['nombre'].lower() == nombre.lower():
            print("Contacto ya existe.")
            return

    contactos.append({"nombre": nombre, "numero": numero, "correo": correo})
    print("Contacto agregado correctamente.\n")

# Función para buscar un contacto por nombre
def buscar_contacto():
    nombre = input("Ingrese el nombre a buscar: ").strip().lower()
    for c in contactos:
        if c['nombre'].lower() == nombre:
            print("\n--- Detalles del Contacto ---")
            print(f"Nombre: {c['nombre']}")
            print(f"Número: {c['numero']}")
            print(f"Correo: {c['correo']}\n")
            return
    print("Contacto no encontrado.\n")

# Función para editar el número o correo
def editar_contacto():
    nombre = input("Nombre del contacto a editar: ").strip().lower()
    for c in contactos:
        if c['nombre'].lower() == nombre:
            nuevo_numero = input("Nuevo número: ").strip()
            nuevo_correo = input("Nuevo correo: ").strip()
            c['numero'] = nuevo_numero
            c['correo'] = nuevo_correo
            print("Contacto actualizado correctamente.\n")
            return
    print("Contacto no encontrado.\n")

# Función para eliminar un contacto
def eliminar_contacto():
    nombre = input("Nombre del contacto a eliminar: ").strip().lower()
    for c in contactos:
        if c['nombre'].lower() == nombre:
            confirm = input(f"¿Eliminar a {c['nombre']}? (s/n): ")
            if confirm.lower() == 's':
                contactos.remove(c)
                print("Contacto eliminado.\n")
            else:
                print("Eliminación cancelada.\n")
            return
    print("Contacto no encontrado.\n")

# Función para mostrar todos los contactos ordenados alfabéticamente
def mostrar_contactos():
    if not contactos:
        print("No hay contactos registrados.\n")
        return
    ordenados = sorted(contactos, key=lambda x: x['nombre'].lower())
    print("\n--- Lista de Contactos ---")
    for c in ordenados:
        print(f"Nombre: {c['nombre']} | Número: {c['numero']} | Correo: {c['correo']}")
    print()

# Menú principal
def menu():
    while True:
        print("=== AGENDA DE CONTACTOS ===")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            buscar_contacto()
        elif opcion == '3':
            editar_contacto()
        elif opcion == '4':
            eliminar_contacto()
        elif opcion == '5':
            mostrar_contactos()
        elif opcion == '6':
            print("Saliendo de la agenda. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()
