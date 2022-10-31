'''n = int(input('Total number of elements:'))
r = int(input('Number of elements to be chosen:'))
n_fact = 1
for i in range(1,n+1):
    n_fact = n_fact * i
r_fact = 1
for i in range(1,r+1):
    r_fact = r_fact * i
n_r_fact = 1
for i in range(1,n-r+1):
    n_r_fact = n_r_fact * i
comb = n_fact//(r_fact * n_r_fact)
print(comb)'''

'''def fact(n):
    n_fact = 1
    for i in range(1,n+1):
        n_fact = n_fact * i
    return n_fact'''


#Tofind all possible cominations with a factorial function
'''n_total = int(input('Total number of elements:'))
r_total = int(input('Number of elements to be chosen:'))'''

#n_fact = fact(n_total)
#r_fact = fact(r_total)
#n_r_fact = fact(n_total - r_total)
#comb = fact(n_total)//(fact(r_total) * fact(n_total - r_total))
#print(comb)

'''def comb(n,r):
    n_com_p = fact(n)//(fact(r)*fact(n-r))
    print(n_com_p)
comb(n_total,r_total)'''

#Return keyword does not print the result but instead tell then result so we can save it in a variable for further use
'''Advantages of functions
Readability
Testing becomes easy 
Avoids repetative code
We can solve problem by dividing it in short snippets
'''

#Examples of functions

#To check prime number
def isPrime(n):
    for i in range(2,n):
        if (n % i == 0):
            break
    else:
        return True
    return False
#isPrime(10)

def primeFrom2toN(n):
    for k in range(2,n+1):
        k_prime = isPrime(k)
        if k_prime:
            print(k)

primeFrom2toN(10)


'''Functions calling

for example if we call function A then B ---> then C and on and on 
so if a contain func B b contain C then in this cas A will wait for B and inturn B will wait for C to complete 
that means if we call A first then it will wait for all the functions to works then at last A will executed 
this thing is called as Last IN first OUT case also known as CALL STACK'''
'''There are 2 types of scope 
global variable ---> variable which is defined outside any functions globally
local variable  ---> variable which is defined inside any function or class'''

a1 = 5  #global variable
def fun():
    b1 = 5   #local variable 
    
#Can't print or use a local variable outside a function or class
#we can access any global variable before the function call

a = 14
def f():
    a=12
f()
print(a)

'''When f() is called, it changes the value of 'a' whose scope is local only limited inside f(). So when print(a) is called, then it takes the value of 'a' which is assigned as global and outputs 14'''

a = 14
def f():
    a = 12
    return a
a = f()
print(a)

'''When f() is called, it changes the value of 'a' whose scope is local only limited inside f() but then the returned value of this function is assigned to global ‘a’. So when print(a) is called, then it takes the value of 'a' which is assigned as global and outputs 12.'''


a=14
def f():
    global a
    a=12
f()
print(a)

'''When f() is called, it changes the value of 'a' whose scope is global, as the global keyword is used to indicate that variable ‘a’ is used in global scope and changes it’s value to 12. So when print(a) is called, then it takes the value of 'a' which is assigned as global and outputs 12.'''

'''In python we can give a default value in a function parameter'''
def add(a,b,c=0):
    return a + b + c
add(2,3,4)
add(2,3)

#Put all the non default value first and then default value





