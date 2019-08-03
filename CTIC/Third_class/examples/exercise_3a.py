# Ejercicio 3a

cadena = input("Ingrese una cadena: ")
longitud = len(cadena)

for i in range(longitud-1, -1, -1):
    print(f"{cadena[i]}", end="")