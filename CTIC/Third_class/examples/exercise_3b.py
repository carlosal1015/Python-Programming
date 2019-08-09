# Ejercicio 3a
cadena = input("Ingrese una cadena: ")
longitud = len(cadena)

for i in range(0, longitud):
    j = longitud-i-1
    print(f"{cadena[j]}", end="")