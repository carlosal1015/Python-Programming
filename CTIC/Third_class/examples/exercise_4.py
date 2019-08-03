# Ejercicio 4
string = input("Ingrese una cadena: ")
longitud = len(string)
i = 0

while (i < longitud):
    if string[i] == 'a':
        print(f"'a' encontrado en la posición {i+1}.")
    i = i + 1

print("Se imprime la cadena: ", end="")
for simb in string:
    print(f"{simb}", end="")

print()