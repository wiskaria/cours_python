correct_word = "Bonjour"
word = ""
tries = 3
while tries > 0:
    word = input("Veuillez entrer 'Bonjour': \n")
    if word != correct_word:
        tries -= 1
    else:
        print("Bravo !")
        exit()
print("J'abandonne !")
