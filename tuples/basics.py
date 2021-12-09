'''If you remove the comma at the end, it will be considered as an int'''
# a = (1,)
# print(type(a))

'''Below is not possible since tuples are immutable'''
# a[0] = 1
# print(a)

a = 1, 2, 3, 4
print(a)
print(a[0])

'''Concat two tuples'''
b = (1, 2, 3, 4, 5)
print(a + b)

'''Repetition'''
c = tuple('abc')
print(c * 3)