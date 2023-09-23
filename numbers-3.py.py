import math

number = input("3 didig intiger")
number = int(number)
digit1 = number // 100
digit2 = (number % 100) // 10
digit3 = number % 10
sum = digit1 + digit2 + digit3
print(sum)