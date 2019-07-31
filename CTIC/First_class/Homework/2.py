from money import Money

factory = Money(amount='0', currency='USD')
factory = Money(eval(input("Ingrese el capital:")), 'USD')
computo = Money(5000, 'USD')
mobiliario = Money(2000, 'USD')

if factory.amount < 0: factory = Money(10000, 'USD')
elif factory.amount <= 20000: factory = Money(20000, 'USD')

resto = factory - (computo + mobiliario)
insumos = incentivos = Money(amount=resto.amount/2, currency='USD')
print(f"Se destinará {insumos.amount} {insumos.currency} para la compra de insumos y {incentivos.amount} {incentivos.currency} para los incentivos del personal.")