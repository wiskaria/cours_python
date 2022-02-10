my_list = [1, 2.4, "oui"]
print(my_list)

my_list.append(True)  # OK
print(my_list)
# my_list += True  # KO
my_list.remove(2.4)
print(my_list)
# my_list.remove(0) # KO
