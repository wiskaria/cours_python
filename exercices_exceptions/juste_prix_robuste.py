from random import randint

price = randint(1, 100)
print(
    "Bienvenue au juste prix ! Essayez de trouver le juste prix compris entre 1 et 100 !"
)
while True:
    try:
        guess = int(input("Entrez un prix : \n"))
        if guess > 100 or guess < 1:
            raise ValueError
    except ValueError:
        print("Votre proposition de prix doit être un entier entre 1 et 100 !")
    except KeyboardInterrupt:
        print("Je m'arrête !")
        exit()
    else:
        if guess < price:
            print("C'est plus.")
        elif guess > price:
            print("C'est moins")
        else:
            print(f"Bravo, le juste prix est bien de {price}!")
            break
