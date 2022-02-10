from random import randint


n = randint(10, 15)  # Le nombre de chiffres à afficher
for i in range(n):
    print(randint(0, 9), end="")
