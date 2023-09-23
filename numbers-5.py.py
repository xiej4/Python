import math

seconds = input("between 0 and 86399 inclusive")
seconds = int(seconds)
hours = seconds // 3600
minutes = (seconds % 3600) // 60
print(hours,minutes)