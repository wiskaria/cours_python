from random import randint


def choose_difficulty():
    while True:
        try:
            difficulty = int(
                input(
                    "Veuillez choisir votre mode de difficulté :\
                \n1. Facile\n2. Normal\n3. Personnalisé\n"
                )
            )
            if difficulty < 1 or difficulty > 3:
                raise ValueError
            return difficulty
        except ValueError:
            print("Vous devez entrer 1, 2 ou 3 !")


def get_max_price(difficulty):
    while True:
        if difficulty != 3:
            return 100
        try:
            max_price = int(input("Veuillez entrer le prix maximal possible : \n"))
            if max_price <= 1:
                raise ValueError
            return max_price
        except ValueError:
            print("Votre prix maximal doit être un entier supérieur à 1 !")


def get_max_tries(difficulty):
    while True:
        if difficulty == 1:
            return 0
        if difficulty == 2:
            return 10
        try:
            max_tries = int(input("Veuillez entrer le nombre d'essais maximal : \n"))
            if max_tries < 0:
                raise ValueError
            return max_tries
        except ValueError:
            print("Votre nombre d'essais doit être un entier positif !")


def show_mode(difficulty):
    if difficulty == 1:
        print("Vous avez choisi le mode facile.")
    elif difficulty == 2:
        print("Vous avez choisi le mode normal.")
    else:
        print("Vous avez choisi le mode personnalisé.")


def init_game(difficulty):
    max_price = get_max_price(difficulty)
    max_tries = get_max_tries(difficulty)
    right_price = randint(1, max_price)
    tries = max_tries
    return max_price, max_tries, right_price, tries


def get_guess(max_price):
    while True:
        try:
            guess = int(input("Entrez un prix :\n"))
            if guess < 1 or guess > max_price:
                raise ValueError
            return guess
        except ValueError:
            print(f"Votre proposition doit être entre 1 et {max_price} !")


def end_game(right_price, win):
    if win:
        print(f"Félicitations, le juste prix était bel et bien de {right_price} !")
    else:
        print(f"Vous n'avez plus d'essais ! Le juste prix était de {right_price} !")


def play():
    try:
        difficulty = choose_difficulty()
        max_price, max_tries, right_price, tries = init_game(difficulty)
        while tries > 0 or max_tries == 0:
            if max_tries != 0:
                print(f"Vous avez {tries} essais restants !")
            guess = get_guess(max_price)
            if guess < right_price:
                print("C'est plus !")
            elif guess > right_price:
                print("C'est moins !")
            else:
                end_game(right_price, True)
                exit()
            tries -= 1
        end_game(right_price, False)
    except:
        print("Fin du programme !")


play()
