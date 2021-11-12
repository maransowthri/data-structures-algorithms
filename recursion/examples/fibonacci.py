import time
from functools import lru_cache


# Memoization - manually caching the results of the recursive calls
cache = {}

def fibonacci(n):
    assert type(n) is int and n >= 0, "Invalid Input"
    if n in cache:
        return cache[n]
    if n in [0, 1]:
        return n
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = res
        return res
# start_time = time.time()
# print(fibonacci(500))
# print("--- %s seconds ---" % (time.time() - start_time))

# Memoization - caching the results with in-built method
@lru_cache(maxsize=1000)
def fibonacci_lru(n):
    assert type(n) is int and n >= 0, "Invalid Input"
    if n in cache:
        return cache[n]
    if n in [0, 1]:
        return n
    else:
        res = fibonacci_lru(n-1) + fibonacci_lru(n-2)
        cache[n] = res
        return res

start_time = time.time()
print(fibonacci_lru(5))
print("--- %s seconds ---" % (time.time() - start_time))

        