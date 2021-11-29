days = input('How many days"s temperature? ')
assert days.isdecimal(), "Uh, Oh! Invalid input!"
days = int(days)
step = 1
temps = []

while step <= days:
    temp = input('Day ' + str(step) + '"s temp: ')
    assert float(temp), "Uh, Oh! Invalid input!"
    temps.append(float(temp))
    step += 1

avg = sum(temps) / len(temps)
print('Average = ' + str(round(avg, 2)))
days_above_temp = 0

for temp in temps:
    if temp > avg:
        days_above_temp += 1

print(str(days_above_temp) + ' day(s) above average')