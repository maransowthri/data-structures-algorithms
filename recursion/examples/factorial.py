def factorial(n):
    assert type(n) is int and n >= 0, 'Invalid Input: ' + n
    if n in [0, 1]:
        return 1

    return n * factorial(n - 1)

print(factorial('hello'))