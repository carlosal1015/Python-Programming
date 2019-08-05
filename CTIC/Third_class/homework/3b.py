def isPrime(number):
	if number == 1:
		print(f"{number} no es primo.")
	else:
		i = 2
		while i**2 <= number:
			if number % i == 0:
				print(f"{number} no es primo.")
				break
			i += 1

def main():
	number = int(input("Ingreso un enterno no negativo: "))
	print(isPrime(number))
# if isPrime(number) == None:
# 	print(4)
# else:
# 	print()
# 	#print(f"{number} es primo.")
if __name__ == "__main__":
    main()
#https://stackoverflow.com/questions/35443199/function-with-if-statements-returns-none
#https://stackoverflow.com/questions/50468597/unable-to-get-return-values-when-in-if-elif-else-python