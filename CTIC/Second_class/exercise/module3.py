from random import randint as rd

i = 0

while i < 20:
    x = rd(1, 6)
    if i % 5 == 0:
        print()
    print(f"{x}", end=" "*10)
    i = i + 1

print()
