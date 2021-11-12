def sum(list_in, index=0):
    if index == len(list_in):
        return 0
    return list_in[index] + sum(list_in, index + 1)

list_in = [1, 2, 3, 4]
print(sum(list_in))
