cadena = input("Ingrese una cadena:")
longitud = len(cadena)

acumulador = ""
for simb in cadena:
    acumulador = simb + acumulador

print(acumulador)