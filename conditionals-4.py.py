person1 = input()
person2 = input()
age1 = input()
age2 = input()
syear1 = age1[6:]
year1 = int(syear1)
syear2 = age2[6:]
year2 = int(syear2)
smonth1 = age1[3:5]
month1 = int(smonth1)
smonth2 = age2[3:5]
month2 = int(smonth2)
sday1 = age1[:2]
day1 = int(sday1)
sday2 = age2[:2]
day2 = int(sday2)
if year1 - year2 < 0:
    print(person1+" is older.")
elif year2 - year1 < 0:
    print(person2+" is older.")
else:
    if month1 - month2 < 0:
        print(person1+" is older.")
    elif month2 - month1 < 0:
        print(person2+" is older.")
    else:
        if day1 - day2 < 0:
            print(person1+" is older.")
        elif day2 - day1 < 0:
            print(person2+" is older.")
        else:
            print("Are you twins or something?")