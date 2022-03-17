from random import randint

difficulty = int(
    input(
        "Veuillez choisir votre mode de difficulté :\n1. Facile\n2. Normal\n3. Personnalisé\n"
    )
)
if difficulty == 1:
    print("Vous avez choisi le mode facile.")
    max_price = 100
    max_tries = 0
elif difficulty == 2:
    print("Vous avez choisi le mode normal.")
    max_price = 100
    max_tries = 10
else:
    print("Vous avez choisi le mode personnalisé.")
    max_price = int(input("Veuillez entrer le prix maximum possible : \n"))
    max_tries = int(input("Veuillez entrer le nombre maximal d'essais possibles : \n"))
print(
    f"Bienvenue au juste prix ! Essayez de trouver le juste prix compris entre 1 et {max_price}!"
)
price = randint(1, max_price)
tries = max_tries
while tries > 0 or max_tries == 0:  # Si max_tries vaut 0, on a des essais illimités
    if max_tries != 0:
        print(f"Vous avez {tries} essais restants !")
    guess = int(input("Entrez un prix : \n"))
    if guess < price:
        print("C'est plus.")
    elif guess > price:
        print("C'est moins")
    else:
        print(f"Bravo, le juste prix est bel et bien de {price} !")
        if max_tries != 0:
            print(f"Vous avez trouvé en {max_tries - tries + 1} essais !")
        input("Appuyez sur entrée pour quitter...")
        exit()
    tries -= 1
print(f"Vous n'avez aucun essai restant ! Le juste prix était de {price}")
input("Appuyez sur entrée pour quitter...")
