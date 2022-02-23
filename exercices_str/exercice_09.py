my_str = "Bonjour tout le monde je suis anticonstitutionnel"

my_list = my_str.split(" ")
print(my_list)
max_length = 0
longest_word = ""
for word in my_list:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word
print(longest_word)
