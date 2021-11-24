import numpy as np

# 1. Create and traverse

arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2D)

for i in range(len(arr2D)):
    for j in range(len(arr2D[i])):
        print(arr2D[i][j])

# 2. Insertion at 0
new_arr = np.insert(arr2D, 0, [[0, 0, 0]], axis=1)
print(new_arr)

# 3. Insertion at the end
new_arr = np.append(arr2D, [[0, 0, 0]], axis=0)
print(new_arr)

# 4. Accessing elements
print(arr2D[0][0])
