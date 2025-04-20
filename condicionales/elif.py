Ingreso = 10000
Gasto = 9000

if Ingreso >= 10000:
    print("ESTAS BIEN EN CUALQUIER PARTE DEL MUNDO")
    if Ingreso - Gasto >= 3000:
        print("ESTAS MÁS QUE BIEN")
    elif Ingreso - Gasto > 1000:
        print("PUEDES SOBREVIVIR")
    else:
        print("PERO CON ESOS GASTOS PARECES POBRE")

elif Ingreso >= 1000:
    print("ESTAS BIEN EN LATAM")
else:
    print("ERES POBRE")