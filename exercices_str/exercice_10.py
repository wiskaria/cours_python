first_string = "kayak"
second_string = "baobab"
third_string = "Ressasser"
my_str = third_string
length = len(my_str)
for i in range(length // 2):
    if my_str[i].lower() != my_str[(length - 1) - i].lower():
        print("Pas un palindrome !")
        exit()
print("C'est un palindrome !")

# Autre solution
# mot = "Kayak"
# mot = mot.lower()
# if mot == mot[::-1]:
#     print("Palindrome")
# else:
#     print("ce n'est pas un Palindrome")
