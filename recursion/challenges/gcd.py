# Without recursion
def gcd(a, b):
    res = 1

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            res = i

    return res

# print(gcd(8, 16))

# with recursion


def gcd_recur(a, b):
    assert type(a) is int and type(b) is int, "Invalid Input"
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if b == 0:
        return a
    return gcd_recur(b, a % b)


print(gcd_recur(98, 56))
