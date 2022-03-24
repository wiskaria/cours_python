def remove_first_last(my_list):
    if len(my_list) <= 0:
        raise ValueError("La liste ne peut pas être vide !")
    return my_list[1:-1]


print(remove_first_last([1, 2, 3, 4, 5]))
print(remove_first_last(["a", "b", "c"]))
print(remove_first_last([5]))
print(remove_first_last([]))
