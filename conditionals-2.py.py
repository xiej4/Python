year = int(input())
if (year % 400 != 0):
    if (year % 100 == 0):
        print("normal year")
    elif (year % 4 != 0):
        print("normal year")
    else:
        print("leap year")
else:
    print("leap year")