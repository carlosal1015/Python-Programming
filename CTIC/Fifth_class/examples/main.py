# Ejemplo de escritura de archivo
objetoArchivo1 = open("file.txt", "r")

line = objetoArchivo1.readline()

while line != "":
    print(line)
    line = objetoArchivo1.readline()


objetoArchivo1.close()