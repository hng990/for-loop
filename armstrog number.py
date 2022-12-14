num = int(input('Enter your number :'))
order=len(str(num))
sum = 0
a=num
for i in range(num):
     digit = num%10
     sum = sum + digit**order
     num=num//10
if (a==sum):
    print("this number is armstrong number",a)
else:
    print("this number is not armstrong number",a)


