my_list = [0, 1, 1, 1, 0, 2, "ok", "ok"]

max_occurences = 0
most_present_element = None

for element in my_list:
    if my_list.count(element) > max_occurences:
        max_occurences = my_list.count(element)
        most_present_element = element

print(most_present_element)
