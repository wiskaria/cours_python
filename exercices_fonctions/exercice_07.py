def divide():
    try:
        premier_nombre = float(input("Entrez votre premier nombre : \n"))
        second_nombre = float(input("Entrez votre second nombre : \n"))
        return premier_nombre / second_nombre
    except ValueError:
        print("Ce n'est pas un nombre !")
    except ZeroDivisionError:
        print("On ne peut pas diviser par zéro !")


print(divide())
