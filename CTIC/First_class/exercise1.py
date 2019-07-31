# Ejercicio 1

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

print("Las operaciones disponibles son:")
print("+...suma")

ope = input("Elija la operacion: ")

if ope == '+':
    res = num1 + num2
    print("La respuesta es: ", res)
elif ope == '-':
    res = num1 - num2
    print("La respuesta es:", res)
elif ope == '*':
    res = num1*num2
    print("La respuesta es: ", res)
elif ope == '/':
    res = num1/num2
    print("La respuesta es: ", res)
else:
    print("error")