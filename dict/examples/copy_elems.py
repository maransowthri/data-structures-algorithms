my_dict = {'name': 'Maran Sowthri Kalailingam', 'age': 25, 'height': 6.1}
# new_dict = my_dict.copy()
new_dict = {**my_dict}
new_dict['age'] = 27
print(new_dict)
print(my_dict)