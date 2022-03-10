try:
    age = input("Veuillez entrer votre âge :\n")
    age = int(age)
except ValueError:
    print("Vous n'avez pas entré un nombre !")
except KeyboardInterrupt:
    print("Ok, ok je m'arrête...")
else:
    try:
        if age < 0:
            raise ValueError
        elif age < 18:
            print("Vous êtes mineur !")
        else:
            print("Vous êtes majeur !")
    except ValueError:
        print("Le nombre doit être supérieur à 0 !")
