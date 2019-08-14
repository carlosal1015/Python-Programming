# Ejercicio 1
# Item a
# Abrir el fichero para lectura
archivo_estudiante = open("datos_estudiante.txt", "r")
lines = archivo_estudiante.readline()

for i in range(6):
    lista = lines.split()
    if len(lista) > 7:
        print(lista[0])
    lines = archivo_estudiante.readline()

# Item b

print(f"Nombre del archivo: {archivo_estudiante.name}")
archivo_estudiante.close()

# Item c
print(f"Contenido del archivo")

archivo_estudiante = open("datos_estudiante.txt", "r")

for line in archivo_estudiante:
    print(line)

archivo_estudiante.close()