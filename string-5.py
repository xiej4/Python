divisor = float(input())
dividend = float(input())
quotient = divisor / dividend
quot = str(float(quotient))
debugger = quot + "000000"
print(debugger)
if quotient < 10:
    ient = "0" + quot
else:
    ient = quot
rounded = ient[:6]
print(rounded)