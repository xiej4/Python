import math

numberz = []
number = int(input())
roller = False
total = 0
for n in range(0, number):
    coaster = float(input())
    numberz.append(coaster)
    if coaster % 2 == 0:
        roller = True
        total = total + numberz[n]
    else:
        roller = False
print(total)
        