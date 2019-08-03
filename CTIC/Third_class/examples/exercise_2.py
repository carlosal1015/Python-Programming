# Ejercicio 2
# Rango de las minúsculas: 97 a 122

from random import randint as rd

N = int(input("Ingrese el valor de N: "))
contador = summation = 0

while(contador < N):
    codigo = rd(97, 122)
    simb = chr(codigo) # letra minuscula
    print(simb, end="") # forma horizontal

    if simb == 'e':
        summation = summation + 1
    contador = contador + 1

print(f"Aparecieron {summation} letras e's.")