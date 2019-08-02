from datetime import datetime as dt
hora_salida = ['09:43', '11:19', '12:47', '14:0', '15:45', '19:00', '21:45']
hora_llegada = ['11:52', '13:31', '15:19', '16:8', '17:55', '21:20', '23:58']
s, l = "Tiempo de partida más caercano es ", "llegada a las s"
horario = {s: hora_salida, l: hora_llegada}
print("Ingrese la hora en formato de 24 horas:")

hora_usuario= input("Hora: ")
minuto_usuario = input("Minutos: ")

now = dt.strptime(hora_usuario+":"+minuto_usuario, "%H:%M")
x = min(hora_salida, key=lambda t: abs(now - dt.strptime(t, "%H:%M")))
#print(x)
index = hora_salida.index(x)
print(hora_llegada[index])
#print(f"{s}{x} {l}.")