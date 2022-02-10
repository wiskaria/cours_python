# Ne modifiez que les lignes commençant par ICI

my_list = [1, 2, 3, 4, 5.0, "haha"]

# Ajoutez une chaine de caractères à la fin de la liste et affichez la liste

my_list.append("chaine")
print(my_list)

# Enlevez la chaine "haha" de la liste et affichez la liste

my_list.remove("haha")
print(my_list)

# Affichez la tranche contenant tous les éléments à partir du troisième

print(my_list[2:])

# Créez une liste nommée week contenant tous les jours de la semaine

week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# Créez une autre liste nommée week_end contenant les deux derniers jours de la semaine.
# Créez-la à partir de la liste week

week_end = week[-2:]

# Créez une liste nommée month contenant 4 fois les jours du lundi au vendredi
# Créez-la à partir de la liste week

month = 4 * week[:-2]

# Affichez les listes week, week_end et month

print(week, week_end, month)
