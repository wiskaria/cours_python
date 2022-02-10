from random import randint


answer = input("Voulez-vous lancer un dé ?\n")

while answer == "oui":
    dice = randint(1, 6)
    print(dice)
    answer = input("Voulez-vous lancer un dé ?\n")
