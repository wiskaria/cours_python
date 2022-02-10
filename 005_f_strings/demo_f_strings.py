# Créons quelques variables
name = "Mounir"
age = 25

# Affichage classique
print("Affichage classique : ")
print("Bonjour, je suis", name, "et j'ai", age, "ans")
print()

# Affichage avec des f-strings
print("Affichage avec f-strings :")
print(f"Bonjour, je suis {name} et j'ai {age} ans")
print()

# Utilisation de len dans le f-string
print("Utilisation de len dans le f-string")
print(f"Mon nom {name} contient {len(name)} lettres")
print()
# Utilisation d'opérations dans le f-string
print("Utilisation d'opérations dans le f-string")
print(f"Mon nom {name} contient {3+3} lettres")
print()

# Créons à présent une variable float

my_float = 3.9415196

# Affichons cette variable avec seulement 2 chiffres décimaux

print(f"{my_float:.2f}")

# # Affichons maintenant 3 chiffres décimaux

print(f"{my_float:.3f}")

# # N'affichons que la partie entière

print(f"{my_float:.0f}")

# Créons deux dernières variables
mon_chiffre = 1000
big_number = 100_000  # 10*10*10*10*10
small_number = 0.000014523


# Affichons-les en notation scientifique

print(f"{big_number:e} est plus grand que {small_number:e}")

# Affichons juste leur ordre de grandeur

print(f"{big_number:.0e} est plus grand que {small_number:.0e}")
print(f"{big_number:.0e} est plus grand que {small_number:.0e}")
