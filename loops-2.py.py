import math

n = int(input())
flag = True
a = math.ceil(n ** (1/2))
for Q in range(2, a):
    if n % Q == 0:
        flag = False
    else:
        flag = True
if flag == True:
    print("Prime")
else:
    print("Not prime")