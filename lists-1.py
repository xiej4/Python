import math

numberz = []
number = int(input())
maximum = -99999999999999999999999999999
minimum = 99999999999999999999999999999
count = 0
total = 0
for n in range(0, number):
    height = int(input("Your height in cm"))
    numberz.append(height)
    if height > maximum:
        maximum = height
    if height < minimum:
        minimum = height
    count = count + 1
    total = total + height
numberz.sort()
avg = total / count
print(avg)
range = maximum - minimum
print(range)