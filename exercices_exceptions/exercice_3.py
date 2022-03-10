try:
    my_list = [1, 2, 3, 4, 5, 6]
    index = input("Quel élément voulez-vous ?\n")
    index = int(index)
    print(my_list[index])
except ValueError:
    print("Votre indice doit être un nombre !")
except IndexError:
    print(f"Votre indice doit se trouver entre {-len(my_list)} et {len(my_list)-1} !")
except KeyboardInterrupt:
    print("Ok, je m'arrête...")
