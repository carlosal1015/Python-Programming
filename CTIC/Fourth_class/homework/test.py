"""
x = "a b c d e f"
x.split()

for i in range(len(x)-1):
    if x[i+1] > x[i]:
        print(x)
"""

def eliminar_elementos(x):
    y = int(input("Ingrese elemento a eliminar:"))
    for j in range(len(x) - 1, -1, -1):
        if x[j] == y:
            del x[j]

l = [2, 2, 5, 2, 3, 2, 4, 2]

eliminar_elementos(l)

print(l)