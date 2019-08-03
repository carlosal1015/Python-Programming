# Ejercicio 1a (sin return)
def mayor_de_tres(numb1, numb2, numb3):
    mayor = numb1
    if mayor < numb2:
        mayor = numb2
    elif mayor < numb3:
        mayor = numb3
    
    print(f"El mayor de los tres es {mayor}.")
    #max(numb1, numb2, numb3)

# Programa principal
a = float(input("Ingrese numero 1: "))
b = float(input("Ingrese numero 2: "))
c = float(input("Ingrese numero 3: "))

#Invocación de la función
print(mayor_de_tres(a, b, c))