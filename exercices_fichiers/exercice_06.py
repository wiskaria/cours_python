# Point b
def get_names():
    names = []
    with open("notes.txt", "r") as file:
        for line in file:
            name_and_note = line.strip().split(":")
            names.append(name_and_note[0])
    return names


# Point c
def get_notes():
    notes = []
    with open("notes.txt", "r") as file:
        for line in file:
            name_and_note = line.strip().split(":")
            notes.append(name_and_note[1])
    return notes


# Point d
def get_note(name):
    names = get_names()
    index = names.index(name)
    return get_notes()[index]


# Point e
def has_passed(name):
    note = get_note(name)
    return note >= 10


# Point f
def get_average():
    average = 0
    notes = get_notes()
    for note in notes:
        average += int(note)
    return average / len(notes)


# Point g
def add_student(name, note):
    with open("notes.txt", "a") as file:
        file.write("\n" + name + ":" + str(note))


print(add_student("Bavo", 0))
