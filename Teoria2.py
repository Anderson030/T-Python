# Explicaciones de Python: Funciones, Excepciones, Tuplas, Ciclos y más

# -----------------------------
# FUNCIONES EN PYTHON
# -----------------------------

# Una función es un bloque de código reutilizable que puede recibir parámetros y retornar valores.
def saludar(nombre):
    """Función que recibe un nombre y devuelve un saludo."""
    return f"Hola, {nombre}!"

print(saludar("Ander"))  # Resultado: Hola, Ander!

# Función sin parámetros
def mensaje():
    print("Bienvenido al sistema de prueba!")

mensaje()

# Función con múltiples parámetros y retorno
def sumar(a, b):
    return a + b

print("Suma:", sumar(3, 5))


# -----------------------------
# EXCEPCIONES EN PYTHON
# -----------------------------

# Manejo de errores para evitar que el programa se detenga por entradas inválidas
try:
    numero = int(input("Ingresa un número entero: "))
    print(f"El doble es: {numero * 2}")
except ValueError:
    print("Error: Debes ingresar un número válido.")


# -----------------------------
# TUPLAS EN PYTHON
# -----------------------------

# Las tuplas son inmutables, útiles para agrupar datos fijos
coordenadas = (10, 20)
print(f"X: {coordenadas[0]}, Y: {coordenadas[1]}")

# Desempaquetado de tupla
nombre, edad = ("Ander", 21)
print(f"Nombre: {nombre}, Edad: {edad}")


# -----------------------------
# LISTAS EN PYTHON
# -----------------------------

# Una lista es una colección de elementos modificables
frutas = ["manzana", "pera", "uva"]
frutas.append("mango")  # Agregar elemento
print("Frutas:", frutas)

# Acceso y modificación
print(frutas[1])  # pera
frutas[1] = "banano"
print("Actualizado:", frutas)


# -----------------------------
# DICCIONARIOS EN PYTHON
# -----------------------------

# Un diccionario almacena pares clave-valor
persona = {"nombre": "Ander", "edad": 21, "activo": True}
print("Nombre:", persona["nombre"])

# Modificar valores
del persona["activo"]
persona["edad"] = 22
print("Diccionario actualizado:", persona)


# -----------------------------
# CICLOS EN PYTHON
# -----------------------------

# Bucle FOR
print("\nUsando for:")
for i in range(5):
    print(f"Número: {i}")

# Bucle WHILE
print("\nUsando while:")
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# BREAK y CONTINUE
print("\nBreak y Continue:")
for i in range(5):
    if i == 3:
        break  # Sale del bucle si i es 3
    if i == 1:
        continue  # Salta cuando i es 1
    print(f"i = {i}")


# -----------------------------
# CONDICIONALES EN PYTHON
# -----------------------------

# Estructuras de decisión para ejecutar bloques dependiendo de condiciones
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres un niño")


# -----------------------------
# OPERADORES BÁSICOS
# -----------------------------

# Aritméticos: +, -, *, /, //, %, **
print("Aritmética básica:", 5 + 2, 5 - 2, 5 * 2, 5 // 2, 5 % 2, 2 ** 3)

# Lógicos: and, or, not
print("Lógicos:", True and False, True or False, not False)

# Comparación: ==, !=, >, <, >=, <=
print("Comparaciones:", 5 > 2, 5 == 5, 3 != 4)


# -----------------------------
# FUNCIONES LAMBDA
# -----------------------------

# Las funciones lambda son funciones pequeñas y anónimas
cuadrado = lambda x: x * x
print("Cuadrado de 4:", cuadrado(4))


# -----------------------------
# BUENAS PRÁCTICAS
# -----------------------------

# - Comentar el código
# - Usar nombres descriptivos para variables y funciones
# - Dividir el código en funciones reutilizables
# - Validar entradas del usuario
# - Mantener el código limpio y legible
