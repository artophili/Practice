## Read input as specified in the question.
## Print output as specified in the question.
'''n=int(input())
j=1
for i in range(1,n+1):
    if i%2!=0:
        while j<=n-i+1:
            print("1",end="")
            j+=1
        print(end="\n")
    elif i%2==0:
        while j<=n-i+1:
            print("0",end="")
            j+=1
        print(end="\n")
    j=1

n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= n - i + 1:
        if i % 2 == 0:
            print('0',end='')
        else:
            print('1',end='')
        j += 1
    print()
    i += 1'''

n = int(input())
i = 1
n1 = n
n2 = n - 1
while i <= n1:
    spaces = 1
    while spaces <= i - 1:
        print(' ',end='')
        spaces += 1
    p= i
    stars = 1
    while stars <= n - i +1:
        print(p,end='')
        p += 1
        stars += 1
    print()
    i += 1

i = 1
while i <= n2:
    spaces = 1
    while spaces <= n - (i + 1):
        print(' ',end='')
        spaces += 1
    p = n - i
    stars = 1
    while stars <= i + 1:
        print(p,end='')
        p += 1
        stars += 1
    print()
    i+=1
