from random import randint, choice


def get_random_word():
    with open("dico.txt", "r") as dico:
        lines = dico.readlines()
        line_number = randint(0, len(lines))
        return lines[line_number].strip()


# Autre solution :
# def get_random_word():
#     with open("dico.txt", "r") as dico:
#         lines = dico.readlines()
#         return choice(lines).strip()


print(get_random_word())
