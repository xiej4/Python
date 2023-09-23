string = input()
space = string.find(" ")
string2 = string[(space + 1):]
space2 = string2.find(" ")
string3 = string2[:(space2)]
string4 = string3.title()
print(string4)