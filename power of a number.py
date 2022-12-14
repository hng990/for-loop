base = int(input('enter the base digit:'))
exponent = int(input('enter the exponent digit:'))
result = 1
for i in range(exponent,0,-1):
    result = result * base
    print(result)