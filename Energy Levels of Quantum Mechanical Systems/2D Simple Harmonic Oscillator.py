from numpy import polyfit, zeros, log

from math import sqrt

from random import randrange, random

import matplotlib.pyplot as plt

import time

t0 = time.time()

def SHO_2D(N, c, D, l):
    
    k = zeros(N)
    
    for i in range(D):
        j = zeros(2)
        n = 0
                
        while random()  > j[0]**2 * (c* (2*l[0] + 1))**2 and random()  > j[1]**2 * (c* (2*l[1] + 1))**2 and n < N:
            
            a = randrange(-1, 2, 2)
            
            j = j + a
            n = n + 1         
        
        for h in range(n):
            k[h] = k[h] + 1
     
    return k
  
  
N = 5600
c = 10**-3
D = 10000
l = [0, 0]


r0 = range(500, 5600 , 1)

#k0 = SHO_2D(N, c, D, l)

#plt.plot(log(k0))

#for o in range(0, 40, 5):
#    for p in range(150, 350, 5):
#        r0 = range(o, p, 1)
#        print o, p, (-polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0], sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]))




mean = 0
lambdas = []
sd = []
variance = 0
p = 0


for i in range(10):
    k0 = SHO_2D(N, c, D, l)
    p = -polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]
    lambdas.append(p)
    print p, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0])
    mean = ((len(lambdas) -1) * mean + p)/len(lambdas)

for i in lambdas:
    variance += ((mean - i)**2)/len(lambdas)

stddev = sqrt(variance)
   

print mean, stddev

t1 = ((time.time() - t0))
print t1



N = 2101
l = [1, 0]

r0 = range(100, 2100 , 1)

mean = 0
lambdas = []
sd = []
variance = 0
p = 0


for i in range(10):
    k0 = SHO_2D(N, c, D, l)
    p = -polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]
    lambdas.append(p)
    print p, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0])
    mean = ((len(lambdas) -1) * mean + p)/len(lambdas)

for i in lambdas:
    variance += ((mean - i)**2)/len(lambdas)

stddev = sqrt(variance)
   

print mean, stddev

t2 = ((time.time() - t0 - t1))
print t2



N = 1251
l = [1, 1]

r0 = range(150, 1250 , 1)

mean = 0
lambdas = []
sd = []
variance = 0
p = 0


for i in range(10):
    k0 = SHO_2D(N, c, D, l)
    p = -polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]
    lambdas.append(p)
    print p, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0])
    mean = ((len(lambdas) -1) * mean + p)/len(lambdas)

for i in lambdas:
    variance += ((mean - i)**2)/len(lambdas)

stddev = sqrt(variance)
   

print mean, stddev

t3 = ((time.time() - t2 - t1 - t0))
print t3


N = 1251
l = [2, 0]

r0 = range(100, 1250 , 1)

mean = 0
lambdas = []
sd = []
variance = 0
p = 0


for i in range(10):
    k0 = SHO_2D(N, c, D, l)
    p = -polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]
    lambdas.append(p)
    print p, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0])
    mean = ((len(lambdas) -1) * mean + p)/len(lambdas)

for i in lambdas:
    variance += ((mean - i)**2)/len(lambdas)

stddev = sqrt(variance)
   

print mean, stddev

t4 = ((time.time() - t3 - t2 - t1 - t0))
print t4


N = 1101
l = [2, 1]

r0 = range(150, 1100 , 1)

mean = 0
lambdas = []
sd = []
variance = 0
p = 0


for i in range(10):
    k0 = SHO_2D(N, c, D, l)
    p = -polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]
    lambdas.append(p)
    print p, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0])
    mean = ((len(lambdas) -1) * mean + p)/len(lambdas)

for i in lambdas:
    variance += ((mean - i)**2)/len(lambdas)

stddev = sqrt(variance)
   

print mean, stddev

t5 = ((time.time() - t4 - t3 - t2 - t1 - t0))
print t5

