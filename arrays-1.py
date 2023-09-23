numberz = []
number = int(input())
for n in range(0, number):
    height = int(input())
    numberz.append(height)
count = 0
total = 0
maximum = -99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
minimum = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
for n in range(0, number):
    total = total + numberz[n]
    count = count + 1
    if numberz[n] > maximum:
        maximum = numberz[n]
    if numberz[n] < minimum:
        minimum = numberz[n]
average = total / count
print(average)
range = maximum - minimum
print(range)