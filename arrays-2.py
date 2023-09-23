import math

numberz = []
number = int(input())
for n in range(0, number):
    height = int(input())
    numberz.append(height)
numberz.sort()
if number % 2 == 0:
    mid = number // 2
    mid1 = mid + 1
    median = (mid + mid1) / 2
else:
    median = math.ceil(number / 2)
print(median)