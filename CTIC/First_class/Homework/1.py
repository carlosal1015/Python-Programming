from datetime import timedelta as tm

hora_salida = [tm(hours=9, minutes=43), tm(hours=11, minutes=19), tm(hours=12, minutes=47), tm(hours=14, minutes=0), tm(hours=15, minutes=45), tm(hours=19, minutes=0), tm(hours=21, minutes=45)]
hora_llegada = [tm(hours=11, minutes=52), tm(hours=13, minutes=31), tm(hours=15, minutes=19), tm(hours=16, minutes=8), tm(hours=17, minutes=55), tm(hours=21, minutes=20), tm(hours=23, minutes=58)]
s, l = "Tiempo de partida más caercano es ", "llegada a las s"
horario = {s: hora_salida, l: hora_llegada}

print("Ingrese la hora en formato de 24 horas:")
hora_usuario = tm(
    int(input("Hora: ")),
    int(input("Minutos: ")),
	)

for i in range(len(hora_salida)):
	tmp = hora_usuario -  hora_salida[i]

print(f"{s} {l}.")