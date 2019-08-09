#Ejercicio 1a (con return)
def convierte(n1):
    n2=n1*9/5+32
    print("T°Celcius"," "*5,"T°Farenheit")
    print(" "*2,n1," "*11,n2)

################################
#Programa principal
status=1
while(status):
    status=0
    temperatura=float(input("Ingrese temperatura de 0°C-100°C: "))
    if temperatura<0 or temperatura>100:
        status=1
#Invocacion a la funcion
convierte(temperatura)
