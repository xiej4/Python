year = input()
month = input()
day = input()
y = len(year)
m = len(month)
d = len(day)
if y == 2:
    raey = "20" + year
else:
    raey = year
if m == 1:
    htnom = "0" + month
else:
    htnom = month
if d == 1:
    yad = "0" + day
else:
    yad = day
date = yad + "/" + htnom + "/" + raey
print(date)