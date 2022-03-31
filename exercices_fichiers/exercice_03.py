def is_in_dico(word: str):
    with open("dico.txt", "r") as dico:
        for line in dico:
            if word.lower() == line.strip().lower():
                return True
        return False


print(is_in_dico("Oui"))
