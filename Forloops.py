'''i=1
while i<5:
    if i == 6:
        break
    print(i,end=" ")
    i = i + 1
else:
    print('Else is also printed')'''
'''i=1
while i<5:
    if i == 3:
        break
    print(i,end='')
    i = i + 1
else:
    print('Else is also printed')'''

#The else block is only executed
#iff the for/while loop is NOT terminated by a break statement
'''n = int(input())
for i in range(1,n+1,1):
    for j in range(i,n+1,1):
        print('*',end='')
    print()'''

n = int(input())
n1 = n // 2 + 1
n2 = n // 2
for i in range(1,n1 + 1):
    print(' '*(n1-i),end='')
    print((2*i-1)*'*',end='')
    print()
for j in range(1,n2+1):
    print(' '*j,end='')
    print((2*(n2-j+1)-1)*'*',end='')
    print()


