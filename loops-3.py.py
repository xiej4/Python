string = input()
n = string.find(" ")
string2 = string[(n+1):]
print(string2)
o = string2.find(" ")
string3 = string2[:o]
string4 = string3.title()
print(string4)