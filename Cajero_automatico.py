# Cajero Automático Simulado
# Permite registrar un usuario, realizar consultas, retiros, consignaciones y ver historial

usuario = {}
historial = []

# Registrar un usuario con nombre y saldo inicial
def registrar_usuario():
    nombre = input("Ingrese su nombre: ").strip()
    try:
        saldo = float(input("Ingrese saldo inicial: "))
        if saldo < 0:
            print("El saldo debe ser positivo.")
            return
        usuario['nombre'] = nombre
        usuario['saldo'] = saldo
        historial.clear()
        historial.append(f"Registro inicial con saldo: ${saldo:.2f}")
        print("Usuario registrado con éxito.\n")
    except ValueError:
        print("Entrada inválida. Ingrese un número válido.\n")

# Consultar saldo actual
def consultar_saldo():
    if not usuario:
        print("Primero debe registrar un usuario.\n")
        return
    print(f"Saldo actual: ${usuario['saldo']:.2f}\n")

# Retirar dinero
def retirar():
    if not usuario:
        print("Debe iniciar sesión primero.\n")
        return
    try:
        monto = float(input("Ingrese monto a retirar: "))
        if monto <= 0:
            print("El monto debe ser mayor que 0.\n")
            return
        if monto > usuario['saldo']:
            print("Fondos insuficientes.\n")
            return
        usuario['saldo'] -= monto
        historial.append(f"Retiro: -${monto:.2f}")
        print(f"Retiro exitoso. Nuevo saldo: ${usuario['saldo']:.2f}\n")
    except ValueError:
        print("Entrada inválida.\n")

# Consignar dinero
def consignar():
    if not usuario:
        print("Debe iniciar sesión primero.\n")
        return
    try:
        monto = float(input("Ingrese monto a consignar: "))
        if monto <= 0:
            print("El monto debe ser mayor que 0.\n")
            return
        usuario['saldo'] += monto
        historial.append(f"Consignación: +${monto:.2f}")
        print(f"Consignación exitosa. Nuevo saldo: ${usuario['saldo']:.2f}\n")
    except ValueError:
        print("Entrada inválida.\n")

# Ver historial de transacciones
def ver_historial():
    if not usuario:
        print("Debe iniciar sesión primero.\n")
        return
    print("\n--- Historial de Transacciones ---")
    for mov in historial:
        print(mov)
    print()

# Menú principal
def menu():
    while True:
        print("\n=== CAJERO AUTOMÁTICO ===")
        print("1. Registrar usuario")
        print("2. Consultar saldo")
        print("3. Retirar dinero")
        print("4. Consignar dinero")
        print("5. Ver historial")
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            consultar_saldo()
        elif opcion == '3':
            retirar()
        elif opcion == '4':
            consignar()
        elif opcion == '5':
            ver_historial()
        elif opcion == '6':
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()
