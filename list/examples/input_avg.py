input_list = []
while True:
    user_input = input('Enter a number: ')
    if user_input == 'done':
        print(sum(input_list) / len(input_list))
        break
    input_list.append(float(user_input))

import datetime
import time

def mystery_func(val=datetime.datetime.now()):
    print(val)

mystery_func()
time.sleep(5)
mystery_func()
time.sleep(5)
mystery_func()
time.sleep(5)
