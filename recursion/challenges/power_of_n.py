def power_of_n(x, n):
    assert type(x) in [int, float] and type(
        n) is int and x >= 0 and n >= 0, "Invalid Input"
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * power_of_n(x, n - 1)


print(power_of_n(3.4, 4))
