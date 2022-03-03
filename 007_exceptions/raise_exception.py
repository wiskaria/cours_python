try:
    x = int(input("Entrez un nombre positif : "))
except:
    print("Ceci n'est pas un nombre !")
else:
    if x < 0:
        raise ValueError("La valeur ne doit pas être négative")
