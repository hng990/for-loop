#fibonacci series meanse give the output in
# the integer sequence of 0, 1, 1, 2, 3, 5, 8.

x = int(input('enter the number to find fibonacci series:'))
n1 = 0
n2 = 1
series = [n1,n2]
if x == 0 :
  print('fibonacci series of this number is:',n1)
else:
  for i in range(0,x-2):
    x = series[i]+series[i+1]
    series.append(x)
  print(series)


   #not work