#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script is used to calculate the closest time.

Author: Oromion
Date: 02/08/2019
"""
from datetime import datetime as dt

hora_salida = ['08:00' ,'09:43', '11:19', '12:47', '14:00', '15:45', '19:00', '21:45']
hora_llegada = ['10:16', '11:52', '13:31', '15:19', '16:08', '17:55', '21:20', '23:58']

print("Ingrese la hora en formato de 24 horas:")

hora_consultada = input("Hora: ")
minuto_consultado = input("Minutos: ")

consulta = dt.strptime(hora_consultada + ":" + minuto_consultado, "%H:%M")
hora_cercana = min(hora_salida, key=lambda t: abs(dt.strptime(t, "%H:%M") - consulta))

index = hora_salida.index(hora_cercana)
print(f"Tiempo de partida más cercano es {hora_cercana}, llegada a las {hora_llegada[index]}")