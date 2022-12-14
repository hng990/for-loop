num = int(input('enter the number:'))
sum = 0
for i in range (2,(num+1)):
    x = 2
    for x in range(2,i):
        if (i % x == 0):
            x = i
            break;
    if x is not i:
        sum = sum+i
print('sum of all prime number is:',sum )
