import math

numberz = []
number = int(input())
for n in range(0, number):
    height = int(input("Your height in cm"))
    numberz.append(height)
numberz.sort()
if number % 2 == 0:
    median = number / 2 - 1
    media1 = number / 2
    median = (median + media1) / 2
else:
    median = math.ceil(number / 2)
naidem = numberz[int(median)]
print(naidem)