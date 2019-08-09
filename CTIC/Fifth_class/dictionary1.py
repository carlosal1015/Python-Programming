mi_dic = dict()
mi_dic

dic2 = {}
dic2

d1 = {1: [1, 2], 3: [3, 4]}
d1

# Los keys deben ser unicos. No puede ser una lista, pero si una tupla

d2 = {(1, 2): 1, (3, 4): 3}
d2

# Los strings son inmutables, se pueden emplear como key en un diccionario.
d3 = {1: "john", 3: "peter"}
d3

d4 = {"john": 1, "peter": 3}
d4

d4["susan"] = 5 # Agregar elemento al diccionario.
d4

d4["peter"] = 5 # Cambio el valor
d4

d4["peter"] +=5
d4

del d4["peter"]
d4

print(len(d4)) # la cantidad de items

print(type(d4.keys()))

print(type(d4.values()))