def first_method():
    second_method()
    print("I am the first method")


def second_method():
    third_method()
    print("I am the second method")


def third_method():
    final_method()
    print("I am the third method")


def final_method():
    print("I am the final method")

# first_method()


def range(n):
    if n < 1:
        print(0)
    else:
        range(n - 1)
        print(n)


range(5)
