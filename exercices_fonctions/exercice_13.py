def num_min(password: str):
    counter = 0
    for letter in password:
        if letter.islower():
            counter += 1
    return counter


def num_maj(password: str):
    counter = 0
    for letter in password:
        if letter.isupper():
            counter += 1
    return counter


def num_non_alpha(password: str):
    counter = 0
    for letter in password:
        if not letter.isalpha():
            counter += 1
    return counter


def len_maj(password: str):
    max_length_sequence = 0
    length_current_sequence = 0
    for letter in password:
        if letter.isupper():
            length_current_sequence += 1
            if length_current_sequence > max_length_sequence:
                max_length_sequence = length_current_sequence
        else:
            length_current_sequence = 0
    return max_length_sequence


def len_min(password: str):
    max_length_sequence = 0
    length_current_sequence = 0
    for letter in password:
        if letter.islower():
            length_current_sequence += 1
            if length_current_sequence > max_length_sequence:
                max_length_sequence = length_current_sequence
        else:
            length_current_sequence = 0
    return max_length_sequence


def score(password):
    length = len(password)
    score_length = length * 4
    score_num_min = (length - num_min(password)) * 3
    score_num_maj = (length - num_maj(password)) * 2
    score_non_alpha = num_non_alpha(password) * 5
    penalite_min = len_min(password) * 2
    penalite_maj = len_maj(password) * 3
    return (
        score_length
        + score_num_min
        + score_num_maj
        + score_non_alpha
        - penalite_min
        - penalite_maj
    )


def get_strength(password):
    total_score = score(password)
    if total_score < 20:
        print("Très faible")
    elif total_score < 40:
        print("Faible")
    elif total_score < 80:
        print("Fort")
    else:
        print("Très fort")


password = "Python123_DevWeb_456"
print(score(password))
