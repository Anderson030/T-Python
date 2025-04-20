def calcular_op(operacion, a,b):
    match operacion:
        case "suma":
            return a + b
        case "resta":
            return a - b 
        case "multiplicacion":
            return a * b
        case "division":
            return a / b if b != 0 else print("No se puede dividir por 0")
        case _:
            return "operacion no valida"
        
operacion = input("Elige una opción entre suma, resta, multiplicación, división:  ").lower()
a = float(input("Ingresa un número: "))
b = float(input("Ingresa el segundo número: "))

print("El resultado es: " , calcular_op(operacion, a,b))
