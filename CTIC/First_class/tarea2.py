from math import sqrt

primer_punto = [eval(input()), eval(input())]
segundo_punto = [1, 0]
tercer_punto = [2, 0]
cuarto_punto = [3, 0]
quinto_punto = [4, 0]

def distance(punto):
	return sqrt((primer_punto[0] - punto[0])**2 + (primer_punto[-1] - punto[-1])**2)

min_distance = min(distance(segundo_punto), distance(tercer_punto), distance(cuarto_punto), distance(quinto_punto))
# TODO: Puede haber más de un punto como respuesta!
if min_distance == :
	print("El punto más cercano")

# TODO: Usar diccionario.