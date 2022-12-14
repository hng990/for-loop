num = str(input('enter the number:'))
for i in range(1,num+1):
    first_digit =int(num[0])
    last_digit =int (num[-1])
    sum = first_digit + last_digit
    print(sum)