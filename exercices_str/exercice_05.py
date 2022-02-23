my_str = "aBcDeF"

for letter in my_str:
    if letter.islower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")


# Ou plus simplement
# print(my_str.swapcase())
