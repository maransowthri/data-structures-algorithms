def open_dolls(n):
    if n == 1:
        print("All dolls are opened")
    else:
        print(n, "dolls left")
        open_dolls(n - 1)

open_dolls(5)