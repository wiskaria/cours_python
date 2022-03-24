def tri_bulle(my_list):
    for i in range(len(my_list) - 1, 1, -1):
        for j in range(0, i):
            if my_list[j + 1] < my_list[j]:
                my_list[j + 1], my_list[j] = my_list[j], my_list[j + 1]
    return my_list


print(tri_bulle([1, 2, 5, -2, 3, 0, -2.2, -9, 23]))
