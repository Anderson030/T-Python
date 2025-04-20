peso = float(input("Ingresa tu peso en KG: "))
estatura = float(input("Ingresa tu estatura en M: "))

imc = peso / (estatura ** 2)

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Deja el bazuco que estás en los huesos.")
elif 18.5 <= imc <= 24.9:
    print("Estás en tu punto, ¡aprobado por la comunidad científica del 'tas rico'!")
elif 25 <= imc <= 29.9:
    print("Uy, la barriga ya te esta tapando el pajarito ")
elif 30 <= imc <= 34.9:
    print("Nivel tanque desbloqueado.")
else:
    print("¡TUMBASTE EL SISTEMA DE LO GORD@ QUE ESTÁS! ")



