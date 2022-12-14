#The highest common factor (H.C.F) or greatest common divisor (G.C.D) of
# two numbers is the largest positive integer that
# perfectly divides the two given numbers. For example, the H.C.F of 12 and 14 is 2.

x = int(input('enter the first number:'))
y = int(input('enter the second number:'))
for i in range(1,min(x,y)):
    if (x % i==0) and (y % i==0)and (i != 1):
        hcf = i
print('HCF of two number is:',hcf)
