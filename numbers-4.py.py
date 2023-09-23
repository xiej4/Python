import math

hour = input("Between 0 and 23 inclusive")
minute = input("Between 0 and 59 inclusive")
hour = int(hour)
minute = int(minute)
minute = hour * 60 + minute
second = minute * 60
print(second)