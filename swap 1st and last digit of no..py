n1 = int(input('enter the first number:'))
n2 = int(input('enter the second number:'))
for i in range(n1,n2):
    temp = n1
    n1 = n2
    n2 = temp
print('swaping of number:',n2,n1)