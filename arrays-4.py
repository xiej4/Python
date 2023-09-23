import math

numberz = []
number = int(input())
for n in range(0, number):
    name = input("Your name")
    height = int(input("Your height in cm"))
    numberz.append(height)
numberz.sort()
if number % 2 == 0:
    median = number / 2 - 1
else:
    median = math.ceil(number / 2)
naidem = numberz[int(median)]
print(naidem)