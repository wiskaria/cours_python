for i in range(3):
    try:  # We try to convert user input to int
        age = int(input("Entrez votre âge : \n"))
    except ValueError:  # We tried to cast a wrong value to int
        print("Valeur incorrecte !")
    else:  # No exceptions in the first try
        print(f"Bonjour, vous avez {age} ans !")
        exit()  # We do the finally then we exit the program
    finally:  # Always executed
        try:
            print(age / 0)
        except ZeroDivisionError:  # We have a zero division error
            print("oops")
        except NameError:  # The variable age does not exist
            print("Vous n'avez pas entré votre age")
