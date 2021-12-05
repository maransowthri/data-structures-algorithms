list_in = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
list_out = []

for i in range(len(list_in[0])):
    temp_list = []
    for j in range(len(list_in) - 1, -1, -1):
        temp_list.append(list_in[j][i])
    list_out.append(temp_list)

print(list_out)