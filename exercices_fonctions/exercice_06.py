def count_words(phrase: str):
    previous_letter = ""
    words = 0
    for letter in phrase:
        if letter.isalpha() and (previous_letter == " " or previous_letter == ""):
            words += 1
        previous_letter = letter
    return words


my_phrase = "Bonjour à tous, je suis une chaîne de caractères très longue ! J'ai beaucoup trop de mots."
print(count_words(my_phrase))
