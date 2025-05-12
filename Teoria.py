# Explicaciones de Python: Funciones, Excepciones, Tuplas y Ciclos

# -----------------------------
# FUNCIONES EN PYTHON
# -----------------------------

# Una función es un bloque de código que realiza una tarea específica y puede ser reutilizado.

def saludar(nombre):
    """Función que recibe un nombre y devuelve un saludo."""
    return f"Hola, {nombre}!"

print(saludar("Ander"))  # Resultado: Hola, Ander!


# -----------------------------
# EXCEPCIONES EN PYTHON
# -----------------------------

# Las excepciones se usan para manejar errores en tiempo de ejecución.

try:
    numero = int(input("Ingresa un número entero: "))
    print(f"El doble es: {numero * 2}")
except ValueError:
    print("Error: Debes ingresar un número válido.")


# -----------------------------
# TUPLAS EN PYTHON
# -----------------------------

# Una tupla es como una lista, pero no se puede modificar (es inmutable).

coordenadas = (10, 20)
print(f"X: {coordenadas[0]}, Y: {coordenadas[1]}")

# Las tuplas son útiles cuando los datos no deben cambiar.
# Ejemplo: (nombre, edad)
usuario = ("Ander", 21)
print(f"Nombre: {usuario[0]}, Edad: {usuario[1]}")


# -----------------------------
# CICLOS EN PYTHON
# -----------------------------

# BUCLE FOR: se usa para repetir un bloque de código un número fijo de veces

print("\nUsando for:")
for i in range(5):  # Repite del 0 al 4
    print(f"Número: {i}")

# BUCLE WHILE: se usa cuando no sabemos cuántas veces repetir, pero sí la condición

print("\nUsando while:")
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Uso de break y continue
print("\nBreak y Continue:")
for i in range(5):
    if i == 3:
        break  # Sale del bucle cuando i es 3
    if i == 1:
        continue  # Salta esta iteración cuando i es 1
    print(f"i = {i}")