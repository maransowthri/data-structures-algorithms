import time
from functools import lru_cache


# @lru_cache(maxsize=1000)
def power_of_two(n):
    if n == 0:
        return 1
    else:
        power = power_of_two(n - 1)
        return power * 2

start = time.time()
print(power_of_two(100))
print(time.time() - start)

def power_of_two_itr(n):
    answer = 1
    while n != 0:
        answer *= 2
        n -= 1
    return answer

start = time.time()
print(power_of_two_itr(100))
print(time.time() - start)