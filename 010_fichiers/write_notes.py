from random import randint


with open("notes.txt", "w") as file:
    names = ["Bao", "Sanja", "Krimel", "Robert", "Nacera", "Mounir"]
    for name in names:
        file.write(name + ":" + str(randint(0, 20)) + "\n")
