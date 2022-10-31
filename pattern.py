'''2 2
   2 2'''
'''n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(n,end='')
        j = j + 1
    print()
    i = i + 1'''

'''n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n:
        print(i,end='')
        j = j + 1
    print()
    i = i + 1'''

n = int(input())
i = 1
n1 = n
n2 = n - 1
while i <= n1:
    spaces = 1
    while spaces <= i - 1:
        print(' ',end='')
        spaces += 1
    stars = 1
    while stars <= n - i +1:
        print(stars,end='')    
        stars += 1
    print()
    i += 1

i = 1
while i <= n2:
    spaces = 1
    while spaces <= n - (i + 1):
        print(' ',end='')
        spaces += 1
    stars = 1
    while stars <= i + 1:
        print(,end='')
        stars += 1
    print()
    i+=16

n=int(input())
startvalue=1
for i in range(1,n+1):
    for j in range(startvalue,startvalue+n):
        print(j,end=" ")
    print()
    if i==(n+1)//2:
        if n%2!=0:
            startvalue=n*(n-2)+1
        else:
            startvalue=n*(n-1)+1
    elif i>(n+1)//2:
        startvalue=startvalue-2*n
    else:
        startvalue=startvalue+2*n

