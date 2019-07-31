# Ejercicio 2

from math import pi as pi

print("""
Bienvenido al Tutor de Geometria!\n
Las figuras disponibles son:\n
a. Cuadrado\n
b. Triangulo\n
c. Circulo\n
""")

option = input("Elija la figura para hallar su area: ")

if option == 'a':
    side = int(input("Ingrese el lado del cuadrado: "))
    print(f"El area del cuadrado es: {side*side} metros cuadrados.")
elif option == 'b':
    basis = float(input("Ingrese la base del triangulo: "))
    height = float(input("Ingrese la alura del triangulo: "))
    print(f"El area del triangulo es: {basis*height*0.5} metros cuadrados.")
elif option == 'c':
    radious = float(input("Ingrese el valor del radio del circulo: "))
    print(f"El area del circulo es {pi*radious*radious} metros cuadrados.")
else:
    print("""
    Error! Los valores deben de ser positivos.\n
    Lo sentimos, vuelva a ejecutar el programa.
    """)