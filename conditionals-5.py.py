today = input()
birthday = input()
stodayear = today[6:]
todayear = int(stodayear)
sbirthdayear = birthday[6:]
birthdayear = int(sbirthdayear)
stodaymonth = today[3:5]
todaymonth = int(stodaymonth)
sbirthdaymonth = birthday[3:5]
birthdaymonth = int(sbirthdaymonth)
stodayday = today[:2]
todayday = int(stodayday)
sbirthdayday = today[:2]
birthdayday = int(stodayday)
difdayz = todayday - birthdayday
difmonthz = todaymonth - birthdaymonth
difyearz = todayear - birthdayear
if difdayz < 0:
    difmonthz = difmonthz - 1
else:
    difmonthz = difmonthz
if difmonthz < 0:
    difyearz = difyearz - 1
else:
    difyearz = difyearz
print(difyearz)