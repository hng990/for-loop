#LCM can be referred to as the Least Common Multiple of two numbers.
# For example, the LCM of two numbers a and b is the smallest positive integer
# that is divisible by both.

x = int(input("enter the first number:"))
y = int(input("enter the second number:"))
for i in range(1,min(x,y)):
    if (x % i==0) and (y % i==0):
     hcf = i
     lcm = (x*y)//hcf
print(lcm)