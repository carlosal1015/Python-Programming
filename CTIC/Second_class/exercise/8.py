
# Ejercicio 2

N = int(input("Ingrese el lado del cuadrado: "))

relleno = input("Ingrese el caracter de relleno: ")

for i in range(1, N*N + 1):
    print(f"{relleno}\t", end="")
    if i % 5 == 0:
        print()
