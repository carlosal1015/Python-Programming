N = int(input("Ingrese el tamano de la tupla: "))

#my_tupla = ( eval(input(f"Elemento de la tupla: {i+1}")) for i in range(N) )

# Parte a
tupla = ()

for i in range(N):
    dato = int(input("Dato = "))
    tupla = tupla + (dato,)

print(tupla)

x = int(input("Elemento a eliminar de la tupla: "))
ind = tupla.index(x) # Captura el indice

t = tupĺa[0:ind] + tupla[ind+1:]

print(t)
