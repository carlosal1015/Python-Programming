def isPrime(n):
	if n ==1:
		return False
	i = 2
	while i**2 <= n:
		if n % i == 0:
			return False
		i += 1
	return True

number = int(input("Ingreso un enterno no negativo: "))

if isPrime(number):
	print(f"{number} es primo.")
else:
	print(f"{number} no es primo.")