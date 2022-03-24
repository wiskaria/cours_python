from random import randint


def get_password(length):
    if length < 0:
        raise ValueError("La longueur de la chaîne ne peut pas être inférieure à 0 !")
    password = ""
    for i in range(length):
        password += str(randint(0, 9))
    return password


print(get_password(6))
