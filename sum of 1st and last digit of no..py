n = int(input('enter the number:'))
n1 = str(n)
for i in range(n):
    first =int(n1[0])
    last = int(n1[-1])
    sum = first + last
print('sum of first and last digit are=',sum)