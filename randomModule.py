import random

'''initialize the random number generator'''
random.seed(a=None)
random.seed(a=23)

'''return an object capturing current internal state og generator''' 
state = random.getstate()
random.setstate(state) #restore the internal state

'''functions'''
random.randbytes(10) #generate 10 random bytes for python 3.9 version

'''for integers'''
val = random.randrange(20,50) #return a single random element
print(val)

random.randint(20,45) #return random integer in range between 20 to 45

random.getrandbits(k) #return a non negative integer with k rand bits (for 3.9)

'''function for sequences'''
random.choice("Akshay") 
random.choices()
random.sample()
random.shuffle()

random.random() #return random float point value in range [0.0,1.0)
random.uniform(20,45) #return  random float number n 
random.triangular(3,4)
random.betavariate() #beat distribution where alpha>0 and beta>0 return value between 0 and 1
random.expovariate(34) #exponential distribution 
random.gammavariate() #gamma distribution
random.gauss(mu,sigma) # Gaussian distribution mu=mean sigma=stand. deviation
random.lognormvariate( #log normal distribution 
random.normalvariate()