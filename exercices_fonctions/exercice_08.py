def get_max(list1, list2):
    list1.sort(reverse=True)
    for number in list1:
        if number in list2:
            return number


list1 = [2, 6, 5, 3, 4, 1, -3, 8]
list2 = [-3, 4, 2, 7]


print(get_max(list1, list2))
