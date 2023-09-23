import math

side1 = input()
side1 = float(side1)
angle = input()
angle = float(angle)
angle = math.radians( angle )
tange = math.tan( angle )
side2 = side1 * tange
side3 = (side1 ** 2 + side2 ** 2) ** (1/2)
print(side2,side3)