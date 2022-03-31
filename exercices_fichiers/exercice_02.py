def get_line(file_name, line_number):
    try:
        with open(file_name, "r") as file:
            for index, line in enumerate(file):
                if index + 1 == line_number:
                    return line
        raise EOFError("Il n'y a pas assez de lignes")
    except FileNotFoundError:
        print("Ce fichier n'existe pas !")


print(get_line("ok.txt", 15))
