texto = input("Ingresa un texto: ")

def contar_palabras(texto):
    return len(texto.split())

resultado = contar_palabras(texto) / 2 

if contar_palabras(texto) > 120:
    print("Loco, no te pedí un testamento") 
    print(f"Dijiste {contar_palabras(texto)} palabras")


else:
    print(f"Para decir esa frase te demorarias {resultado} segundos ")
    print(f"Dijiste {contar_palabras(texto)} palabras")
    

