# -----------------------------
# FUNCIONES LAMBDA (Avanzado)
# -----------------------------

# Una función lambda es una función pequeña y sin nombre
cuadrado = lambda x: x * x
print("Cuadrado de 4:", cuadrado(4))

# Con map(): aplica la función lambda a cada elemento
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Cuadrados con map:", cuadrados)

# Con filter(): filtra los elementos que cumplen la condición
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares con filter:", pares)

# Con sorted(): ordena usando lambda como clave
personas = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Marta", "edad": 35},
]
personas_ordenadas = sorted(personas, key=lambda p: p['edad'])
print("Personas ordenadas por edad:")
for p in personas_ordenadas:
    print(p)

# Combinando lambda y condicional en una sola línea
mayor_edad = lambda edad: "Mayor de edad" if edad >= 18 else "Menor de edad"
print("Clasificación:", mayor_edad(20))
