"""
# * pattern program
for i in range(1,6,1):
    print(i *'*')


#output :
#   *
#   **
#   ***
#   ****
#   *****
=================================================
# number pattern peogram
for i in range(1,6):
    for j in range(1,i+1):
       print(j,end = ' ')
    print()
#output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
==============================
for i in range(6,0,-1):
    for j in range (1,i+1):
        print(j,end = ' ')
    print()

#output:
#  1 2 3 4 5
#  1 2 3 4
#  1 2 3
#  1 2
#  1
======================================
for i in range(1,7):
    for j in range(1,i):
        print(j,end=' ')
    print()

#output:
#    1
#    1 2
#    1 2 3
#    1 2 3 4
#    1 2 3 4 5
=========================================
for i in range(6):
    for j in range(i):
        print(i,end=' ')
    print()

# output:
#    1
#    2 2
#    3 3 3
#    4 4 4 4
#    5 5 5 5 5

========================================
for i in range(5,0,-1):
    for j in range(i):
        print(i,end=' ')
    print()

#output:
#    5 5 5 5 5
#    4 4 4 4
#    3 3 3
#    2 2
#    1
=================================
for i in range(6):
    print(i * ' 5 ')

#output:
#     5
#     5  5
#     5  5  5
#     5  5  5  5
#     5  5  5  5  5
=========================================
for i in range(6,0,-1):
    print(i * ' 5 ')

#output:
#     5  5  5  5  5
#     5  5  5  5
#     5  5  5
#     5  5
#     5
==============================
for i in range(7,0,-2):
    for j in range(i):
        print(i,end=' ')
    print()

#output:
#    7 7 7 7 7 7 7
#    5 5 5 5 5
#    3 3 3
#    1

===========================
for i in range(5,0,-1):
    print(i * ' * ')

# output:
#     *  *  *  *  *
#     *  *  *  *
#     *  *  *
#     *  *
#     *
============================
for i in range(0,5):
    for j in range(0,5-i-1):
        print(end='  ')
    for j in range(0,i+1):
        print('*',end="   ")
    print()

#output:

        *
      *   *
    *   *   *
  *   *   *   *
*   *   *   *   *

================================
for i in range(7,0,-2):
    for j in range(0,7-i-1):
        print(end=' ')
    for j in range(1,i+1):
        print('*', end=' ')
    print()

#output:
#    * * * * * * *
#     * * * * *
#       * * *
#         *
=============================================
"""
