print("\nSeccion A")
print("Problema 4")
#Ejercicio 4a(con return)
def primo(number):
    cont=0
    if number<=1:
        return 0
    for i in range(1,number+1):
        if number % i == 0:
            cont=cont+1
    if cont==2:
        return 1
    else:
        return 0
################################
#Programa principal
number=int(input("Ingrese número: "))
    
#Invocacion a la funcion
val=primo(number)
if val == 1:
    print("Es primo")
else:
    print("No es primo")
##################################
#################################
print("\nSeccion B")
print("Problema 4")
#Ejercicio 4b(sin return)
def esprimo(num):
    conteo=0
    if num<=1:
        valor=0
    for j in range(1,num+1):
        if num % j == 0:
            conteo=conteo+1
    if conteo==2:
        valor=1
    else:
        valor=0

    if valor == 1:
        print("Es primo")
    else:
        print("No es primo")
################################
#Programa principal
num=int(input("Ingrese número: "))
    
#Invocacion a la funcion
esprimo(num)


