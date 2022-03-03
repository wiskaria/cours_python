nombre = input("Entrez un nombre : ")
try:
    nombre = int(nombre)
    print(nombre / 0)
except ValueError:
    print("Désolé la valeur saisie n'est pas un nombre.")
