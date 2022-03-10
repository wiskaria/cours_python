try:
    premier_nombre = int(input("Veuillez entrer votre premier nombre : \n"))
    deuxieme_nombre = int(input("Veuillez entrer votre second nombre : \n"))
except ValueError:
    print("Vous n'avez pas entré un nombre !")
    exit()
try:
    if premier_nombre == deuxieme_nombre:
        raise ValueError
    print(f"Le résultat vaut {premier_nombre/deuxieme_nombre}")
except ValueError:
    print("Vous devez entrer deux nombres différents !")
except ZeroDivisionError:
    print("On ne peut pas diviser par zéro !")
