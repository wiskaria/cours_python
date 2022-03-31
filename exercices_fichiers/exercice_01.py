def write_numbers(file_name, max_number=10):
    with open(file_name, "w") as file:
        for i in range(1, max_number + 1):
            file.write(str(i) + "\n")


write_numbers("test.txt", 20)
