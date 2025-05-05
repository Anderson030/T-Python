Funciones 
-Funciones Main 

Entradas = 01
Proceso = 02 03
Salida = 04 

----------------------------------------------------
Una función es un bloque de código que realiza una actividad, soluciona un problema, realiza un proceso. Esta se puede llamar cuantas veces quiera y sirve para reutilizar el código.

Ejemplo

def print_hello_world : 
  print("Hello world")

---------------------------------------------------------
  Una función en py siempre se define con ----DEF---
Métodos tipo BOY SON LOS QUE NO RETORNAN NADA

def main(): = Es el método principal  
    
-----------------------------  
como armar una función 
definir que es una función con def
ponerle nombre a al función
parametros 
return
----------------------------------------
Variables globales y locales 
----------------------------------------

Definir el metodo main y dentro de ese metodo va toda la lógica
-------------------------------------------------------

TODO ESTO LLAMARLO A UNA FUNCION MAIN

nombre= input("Enter your name: ")
def greet(nombre):
    print(f"Hello {nombre}")
greet(nombre)


num1= int(input("Enter number 1: "))
num2= int(input("Enter number 2: "))
def sum(num1,num2):
    return num1 + num2
print("Result: ", sum(num1, num2))


radio = float(input("enter radio: "))
def a_circle(radio):
    pi = 3.1416
    return pi * radio **2
print("The area of ​​the circle is: ", a_circle(radio))


number = int(input("Enter number: "))
def is_par(number):
    return number % 2 == 0
print("¿Is par?", is_par(number))


a = int(input("Enter number 1: "))
b = int(input("Enter number 1: "))
c = int(input("Enter number 1: "))

def count_number(a ,b, c):
    return max(a,b,c)
print("The oldest is: ", count_number(a,b,c))
