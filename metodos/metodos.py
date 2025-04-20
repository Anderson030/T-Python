cadena1 = "Anderson Blandon"
cadena2 = "Hola " + cadena1

#Los metodos tienen el orden de = dato.metodo()

#convierte a mayuscula
resultado1 = cadena2.upper()
#convierte a minusculas
resultado2 = cadena2.lower()
#primera letra en mayuscula
resultado3 = cadena2.capitalize()
#busqueda find, nos indica el número del caracter que queremos buscar, si no lo encontramos, nos da -1
resultado4 = cadena1.find("B")
# Len contamos cuantos caracteres tiene una cadena 
resultado5 = len(cadena2)
# replace nos cambia una cadena por otra nueva que le demos
resultado6 = cadena1.replace("son", "sin")
#Buscamos una cadena en otra cadena, si no hay coincidencia arroja -1
resultado7 = cadena1.index("A")


print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado7)

