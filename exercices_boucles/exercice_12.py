from random import randint


word = ""
while word != "quit":
    word = input("Entrez une commande.")
    if word == "dice":
        print(randint(1, 6))
    elif word == "sum":
        sum = 0
        for i in range(101):
            sum += i
        print(sum)
    elif word == "password":
        n = randint(10, 15)
        for i in range(n):
            print(i, end="")
        print()
    elif word == "quit":
        exit()
    else:
        print("Pas compris !")
