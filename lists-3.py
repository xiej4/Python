import math

numberz = []
number = int(input())
total = 0
for n in range(0, number):
    item = int(input("A number"))
    numberz.append(item)
    if item % 2 == 0:
        total = total + item
    else:
        total = total
print(total)