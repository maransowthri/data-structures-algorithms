def to_binary(n):
    assert type(n) is int, "Invalid Input"
    if n in [0, 1]:
        return n
    return n % 2 + 10 * to_binary(int(n / 2))


print(to_binary(-8))
