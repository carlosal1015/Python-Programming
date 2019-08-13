"""
#Problema2_Listas
cadena=input("Ingrese la palabra:")
##a)
print("Parte A-Imprime en orden contrario")
lista=[]
lista2=[]
lista=cadena.split()
lista2=cadena.split()

for i in range(-1,-len(lista)-1,-1):
    print(lista[i],end=' ')
print()
"""
##c)
cadena=input("Ingrese la palabra:")
lista=[]
lista2=[]
lista2=cadena.split()
print("\nParte C-Elimina la palabra repetida")
frase2=" ".join(lista2)
print("antes: ",frase2)
lista2_nueva=[]
for i in lista2:
    if i not in lista2_nueva:
        lista2_nueva.append(i)

frase2_actual=" ".join(lista2_nueva)
print("despues: ",frase2_actual)
"""
##f)
print("\nParte F-Elimina la letra del centro")
lista3=[]
lista3=input("Ingrese palabra: ")
tam=len(lista3)
indice=int((tam-1)/2)
print(ord(lista3[0]))
lista3_nueva=[]
for i in range(0,len(lista3)):
    lista3_nueva.append(ord(lista3[i]))

print(lista3_nueva)

if tam%2==0:
    print("La palabra es par")
else:
    print("La palabra es impar, eliminemos la letra del centro:")
    lista3_nueva.pop(indice)
print(lista3_nueva)

lista4_nueva=[]
for i in range(0,len(lista3_nueva)):
    lista4_nueva.append(chr(lista3_nueva[i]))
print(lista4_nueva)
frasen=" ".join(lista4_nueva)
print(frasen)
"""