def pyramide(height):
    spaces = height - 1
    stars = 1
    for i in range(1, height + 1):
        print_spaces(spaces)
        print_stars(stars)
        print_spaces(spaces)
        print()
        spaces -= 1
        stars += 2


def print_stars(number):
    for i in range(number):
        print("*", end="")


def print_spaces(number):
    for i in range(number):
        print(" ", end="")


pyramide(3)
# print_stars(5)
# print()
# pyramide(10)
# print()
# pyramide(2)
