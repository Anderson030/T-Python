usuarios = ["Anderson", "Alejandra", "Mateo", "Luis", "Juan"]
contraseñas = [1021, 2021, 2022, 2023, 2024]

 
usuario = input("Ingresa el usuario ")
contraseña = int(input(usuario + " Ingresa la contraseña "))
Bienvenida = f"Buenas tardes {usuario} ¿Cómo estas?, estamos iniciando..."

if usuario in usuarios:
    indice = usuarios.index(usuario)
    if contraseña == contraseñas[indice]:
        print(Bienvenida)
    else:
        print("Contraseña incorrecta", usuario)
else:
    print("No estas en la base de datos", usuario)
    
    
