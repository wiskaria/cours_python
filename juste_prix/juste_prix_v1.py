from random import randint

price = randint(1, 100)
print(
    "Bienvenue au juste prix ! Essayez de trouver le juste prix compris entre 1 et 100 !"
)
while True:
    guess = int(input("Entrez un prix : \n"))
    if guess < price:
        print("C'est plus.")
    elif guess > price:
        print("C'est moins")
    else:
        print(f"Bravo, le juste prix est bien de {price}!")
        break
input("Appuyez sur entrée pour quitter...")
