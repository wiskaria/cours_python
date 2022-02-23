first_string = "abcdeF"
second_string = "123456"
third_string = ".!/"

my_str = first_string

if my_str.isalpha():
    print("Que des lettres")
elif my_str.isnumeric():
    print("Que des chiffres")
elif not my_str.isalnum():
    print("Que des caractères spéciaux")
