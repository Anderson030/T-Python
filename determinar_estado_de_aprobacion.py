# Muestra un mensaje inicial explicando el propósito del programa
print("Programa para determinar si un estudiante aprueba o reprueba.")

# Crea una lista vacía para almacenar tuplas con la calificaciON Y EL ESTADOO
historial = []

# Inicia un ciclo que se repetira indefinidamente hasta que el usuario escriba "salir"
while True: 
    # Solicita al usuario que ingrese una calificación o salir para que el programa termine
    entrada = input("Ingresa una calificación del 0 al 100 (o escribe 'salir' para terminar): ")
    
    # Verifica si el usuario si el usuario salio
    if entrada.lower() == 'salir':
        # Muestra la las calificaciones
        print("\n calificaciones:")
        for item in historial:
            # Imprime cada calificación junto con su estado
            print(f"Nota: {item[0]}, Estado: {item[1]}")
        # Sale del ciclo (y del programa)
        break
    
    # Verifica si lo ingresado no es un número (solo permite dígitos)
    if not entrada.isdigit():
        print(" Ingresa solo números entre 0 y 100.")
        # Salta a la siguiente iteración del ciclo sin ejecutar lo demás
        continue
    
    # Convierte la entrada a un número entero
    nota = int(entrada)

    # Valida que la calificación esté en el rango permitido (0 a 100)
    if nota < 0 or nota > 100:
        print(" Calificación fuera del rango permitido.")
        # Si está fuera del rango, vuelve a pedir otra entrada
        continue

    # Determina si la nota es aprobatoria o no
    if nota >= 60:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    
    # Crea una tupla con la nota y su estado
    resultado = (nota, estado)
    
    # Agrega la tupla a la lista 'historial' para conservar el registro
    historial.append

    print(f" Resultado: {estado}\n")

