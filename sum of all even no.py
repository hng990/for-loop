num = int(input("enter the number:"))
sum = 0
for i in range(2,num+1):
     if i%2 ==0:
         sum = sum + i
         print(sum)