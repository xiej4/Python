entire = input()
if (len(entire) == 13):
    number = entire[5:]
    location = entire[:3]
elif (len(entire) == 9):
    number = entire[1:]
else:
    print("not valid")
space = entire.find(" ")
if (location == "852"):
    if (space == 3):
        pass