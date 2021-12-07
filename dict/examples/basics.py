my_dict = {'name': 'Maran Sowthri Kalailingam', 'age': 25, 'employed': True, 'address': '113 Indra Nagar Sivaganga'}

# Traversing Keys
for key in my_dict:
    print(key, my_dict[key])

# Traversing Values
for value in my_dict.values():
    print(value)

# Traversing Keys & Values
for key, value in my_dict.items():
    print(key, value)

# Check key existence
print('name' in my_dict)

# Delete particular item
print('Delete or Remove an element')
my_dict.pop('name')
# OR
del my_dict['name']
print(my_dict)

# Delete random pair
print('Delete random pair')
print(my_dict.popitem())
print(my_dict)

# Clear all elements of a dictionary
print('Clear all elements of a dictionary')
my_dict.clear()
print(my_dict)

# Delete complete dict
print('Delete complete dict')
del my_dict