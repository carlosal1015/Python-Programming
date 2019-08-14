archivo_estudiante = open("datos_estudiante.txt", "r")

line = archivo_estudiante.readline()

while line != "":
    lista = line.split()    # Pasamos toda la fila a una lista
    summation = 0
    for grade in lista[1:]:
        summation += int(grade)  # Suma todas las notas de un alumno
    mean = summation / len(lista[1:])
    print(f"Alumno {lista[0]}\t Promedio: {mean}.")
    line = archivo_estudiante.readline()

archivo_estudiante.close()