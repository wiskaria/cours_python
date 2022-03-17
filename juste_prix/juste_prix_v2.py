from random import randint

price = randint(1, 100)
print(
    "Bienvenue au juste prix ! Essayez de trouver le juste prix compris entre 1 et 100!"
)
max_tries = 10
tries = max_tries
while tries > 0:
    print(f"Vous avez {tries} essais restants !")
    guess = int(input("Entrez un prix : \n"))
    if guess < price:
        print("C'est plus.")
    elif guess > price:
        print("C'est moins")
    else:
        print(f"Bravo, le juste prix est bel et bien {price} !")
        print(f"Vous avez trouvé en {max_tries - tries + 1} essais !")
        input("Appuyez sur entrée pour quitter...")
        exit(0)
    tries -= 1
print(f"Vous n'avez aucun essai restant ! Le juste prix était de {price}")
input("Appuyez sur entrée pour quitter...")
