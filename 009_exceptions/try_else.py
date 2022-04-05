numerateur = input("Entrez le numérateur : ")
denominateur = input("Entrez le dénominateur : ")
try:
    numerateur = int(numerateur)
    denominateur = int(denominateur)
    result = numerateur / denominateur
except ValueError:
    print("Désolé la valeur saisie n'est pas un nombre.")
except ZeroDivisionError:
    print("On ne peut pas diviser par zéro !")
else:
    print(f"Le résultat de la division vaut {result} !")
