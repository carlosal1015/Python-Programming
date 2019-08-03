"""
Elabore un algortimo que calcule y muestre la suma de todos los multiplos de 5 comprendidos entre dos valores A y B (ambos inclusive). El programa no permitira introducir valores negativos para A y B y verificara que A es menor que B/ Si A es mayor que B, intercambiara sus valores.
"""
A, B = int(input("Valor de A: ")), int(input("Valor de B: "))
if (A<0 or B<0):
    print("Los valores no pueden ser negativos.")

sum = n = 0

if B < A:
    A, B = B, A

while (n >= A and n <= B):
    if n % 5 == 0:
        sum = sum + n
    n = n +1

print(f"La suma de todos los multiplos de 5 entre {A} y {B} es {sum}.")
