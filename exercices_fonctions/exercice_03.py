from random import randint


def create_list(size):
    if size < 0:
        raise ValueError("Votre liste doit avoir une taille positive !")
    my_list = []
    for i in range(size):
        my_list.append(randint(1, 10))
    return my_list


print(create_list(5))
print(create_list(1))
print(create_list(0))
print(create_list(15))
print(create_list(-2))
