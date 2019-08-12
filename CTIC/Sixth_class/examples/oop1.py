from Ejemplo import Articulo
from money import Money

mota = Articulo(cd = 'A001', ct = 10, pr = '1') # Llamada al constructor init.
celular = Articulo(cd = 'A002', ct = 5, pr = '80')

print(mota.status())
print(celular.status())

mota.comprar(10)
celular.vender(2)

print(mota.status())
print(celular.status())
# Un metodo esta asociado a un objeto. Una funcipn no esta asociado a un objeto