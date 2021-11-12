def sum_of_digits(n):
    assert type(n) is int and n > 0, "Invalid Input"
    if 0 <= n <= 9:
        return n
    return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(11111))
