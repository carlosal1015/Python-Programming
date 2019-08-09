"""
from statistics import mean

N = int(input("Ingrese la cantidad de números enteros: "))

#lista = [ int(input(f"Ingrese el N° {i+1} ")) for i in range(N)]

void_list = [None]*N

for i in range(N):
    dato = int(input("Dato = "))
    void_list[i] = dato

print(void_list)

void_list.remove(min(void_list))
void_list.remove(min(void_list))

print(void_list)

print("Numeros sobre el promedio")

summation = 0

for item in void_list:
    if item > mean(void_list):
        print(item, end=" ")
        summation += 1

print()
print(f"La suma de los mayores que el promedio es {summation}.")
"""
aviso = "El examen de admision eva del 5 al 9 de agosto"
lista = aviso.split()
print(lista)

frase = " ".join(lista)
print(frase)
frase2 = "-".join(lista)
print(frase)
