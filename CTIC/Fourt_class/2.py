from statistics import mean

N = int(input("Ingrese la cantidad de números enteros: "))

#lista = [ int(input(f"Ingrese el N° {i+1} ")) for i in range(N)]

void_list = []

for i in range(N):
    dato = int(input("Dato = "))
    void_list.append(dato)

print(void_list)

void_list.remove(min(void_list))
void_list.remove(min(void_list))

print(void_list)

print("Numeros sobre el promedio")

summation = 0

for item in void_list:
    if item > mean(void_list):
        print(item, end="")
        summation += 1

print(summation)
