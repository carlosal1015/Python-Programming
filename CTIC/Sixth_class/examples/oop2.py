from nuevoejemplo import Articulo1
from money import Money

art1 = Articulo1(
    cd = input(f"Ingrese el código: "),
    ct = int(input(f"Ingrese la cantidad: ")),
    pr = eval(input(f"Ingrese el precio unitario: "))
    )

print(f"Se tienen {art1.cantidad()}.")
print(f"Precio unitario {art1.pre}.")