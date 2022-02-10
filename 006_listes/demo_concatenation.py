# Créons une liste et un string
my_list = [1, 2.4, "Bonjour"]
my_str = "Ceci est une chaine de caracteres"

# Concaténons le string à la liste
my_list += my_str  # OK
print(my_list)

# Recréons les variables
my_list = [1, 2.4, "Bonjour"]
my_str = "Ceci est une autre chaine"

# Concaténons la liste au string
my_str += my_list  # KO
