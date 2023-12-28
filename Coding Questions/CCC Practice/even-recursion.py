def even_list(list):
    if (list == []):
        return 0
    else:
        if (list[0] % 2 == 0):
            return even_list(list[1:]) + 1
        return even_list(list[1:])

print(even_list([5, 8, 5, 4, 0, 3, 8]))