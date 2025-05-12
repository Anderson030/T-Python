# Calculadora de Nómina Simple
# Permite registrar empleados, calcular salario neto y mostrar resumen de nómina

empleados = []

# Registrar un nuevo empleado
def registrar_empleado():
    nombre = input("Nombre del empleado: ").strip()
    try:
        horas = float(input("Horas trabajadas: "))
        valor_hora = float(input("Valor por hora: "))
        if horas < 0 or valor_hora <= 0:
            print("Horas y valor deben ser positivos.\n")
            return
        salario_bruto = horas * valor_hora
        retencion = salario_bruto * 0.08
        salario_neto = salario_bruto - retencion

        empleados.append({
            "nombre": nombre,
            "horas": horas,
            "valor_hora": valor_hora,
            "bruto": salario_bruto,
            "retencion": retencion,
            "neto": salario_neto
        })
        print(f"Empleado {nombre} registrado con éxito.\n")
    except ValueError:
        print("Entrada inválida. Use números válidos.\n")

# Mostrar la nómina completa
def mostrar_nomina():
    if not empleados:
        print("No hay empleados registrados.\n")
        return

    total_bruto = total_retencion = total_neto = 0

    print("\n--- Nómina de Empleados ---")
    for e in empleados:
        print(f"Nombre: {e['nombre']}")
        print(f"  Horas: {e['horas']} | Valor Hora: {e['valor_hora']}")
        print(f"  Salario Bruto: ${e['bruto']:.2f}")
        print(f"  Retención (8%): ${e['retencion']:.2f}")
        print(f"  Salario Neto: ${e['neto']:.2f}\n")

        total_bruto += e['bruto']
        total_retencion += e['retencion']
        total_neto += e['neto']

    print("--- Totales Generales ---")
    print(f"Total Bruto: ${total_bruto:.2f}")
    print(f"Total Retención: ${total_retencion:.2f}")
    print(f"Total Neto: ${total_neto:.2f}\n")

# Menú principal
def menu():
    while True:
        print("=== CALCULADORA DE NÓMINA ===")
        print("1. Registrar empleado")
        print("2. Mostrar nómina")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            registrar_empleado()
        elif opcion == '2':
            mostrar_nomina()
        elif opcion == '3':
            print("Saliendo del sistema de nómina.\n")
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()