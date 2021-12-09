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
my_dict.pop('name')
my_dict.pop('name1', 'N/A')
# OR
# del my_dict['name']
print(my_dict)

# Delete random pair
print(my_dict.popitem())
print(my_dict)

# Clear all elements of a dictionary
# my_dict.clear()
print(my_dict)

# Delete complete dict
# del my_dict

# Create new dict with the provided keys and value
new_dict = dict.fromkeys(['is_hiring', 'is_manager', 'is_lead'], False)
print(new_dict)

# Return a default value if the searched key doesn't exist
new_dict['location'] = 'madurai'
print(new_dict.get('location', 'sivaganga'))

# Finding length
print(len(new_dict))

# Adding a new pairs to dict only if that doesn't exist
new_dict.setdefault('location1', 'New Location')
print(new_dict)

# Update
new_dict.update({'location': 'Sivaganga'})
print(new_dict)

# all method on dict just checks all keys
bool_dict = {3: False, 1: True, 2: True}
print(all(bool_dict))

# any method on dict just checks all keys
bool_dict = {'': False, 0: True, 1: True}
print(any(bool_dict))

# Sorted
new_dict = {'name': 'Maran', 'age': 25, 'address': '113 Karumanthakudi Sivaganga'}
print(sorted(new_dict, reverse=True, key=lambda item: len(item)))