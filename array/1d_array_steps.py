from array import array

# 1. Create and traverse an array.
arr = array('i', [1, 2, 3, 4, 5])
arrFloat1D = arr('d', [1.3, 2.3, 3.5, 4.2, 5.6])

for val in arr:
    print(val)

# 2. Insertion
arr.insert(0, 0)
arr.append(6)

print(arr)

# 3. Add items from list
arr.extend([7, 8, 9])
print(arr)

# 4. Remove item
arr.remove(4)
print(arr)

# 5. Remove item by index
arr.pop(1)
print(arr)

# 6. Find the index of an item
print(arr.index(3))

# 7. reverse the array
# in place
arr.reverse()
print(arr)
# as a new array
print(arr[::-1])

# 8. Find where the array is located in memory
print(arr.buffer_info())

# 9. number of occurrences of an item
print(arr.count(3))

# 10. array to string
print(arr.tostring())
print(''.join(map(str, arr)))
