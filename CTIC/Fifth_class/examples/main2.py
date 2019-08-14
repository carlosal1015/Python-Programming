objetoArchivo1 = open("file.txt", "r")
objetoArchivo2 = open("copia2.txt", "w")

line = objetoArchivo1.readline()

while line != "":
    objetoArchivo2.write(line)
    line = objetoArchivo1.readline()

objetoArchivo1.close()
objetoArchivo2.close()