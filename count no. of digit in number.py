"""
# it does not give output
num = int(input('enter the number:')
count = 0
for i in str(num):
    count = count +1
     print(count[i])

===============================
num = input('enter the number:')
lenght = len(num)
if num.isnumeric():
    for i in (range(1,lenght+1)):
       print(end='')
    print(i)
else:
    print('given input is not number')

#############################################
l1=[1,2,3]
l2 = [1,2,3]
l = l1 and l2
print(l)
#o/p:[1,2,3]
=============================================
"""
#fibonacci series
num = 2
s = 0#for first element
f = 1#for second element
if num < 0:
    print('fibonacci series is not applicable on this number:')
for i in range(1,num-1):
    fibo_series = i+(i+1)
print(fibo_series)


