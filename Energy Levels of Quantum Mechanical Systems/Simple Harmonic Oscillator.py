from numpy import polyfit, zeros, log

from math import sqrt

from random import randrange, random

import matplotlib.pyplot as plt

import time

t0 = time.time()

def k_SHO(N, c, D, l, m):
    
    k = zeros(N)
    
    for i in range(D):
        j = 0
        n = 0
                
        while random()  > j**2 * (c* (2*l + 1))**2 and n < N:
            
            a = randrange(-1, 2, 2)
            
            j = j + a
            n = n + 1         
        
        for h in range(n):
            k[h] = k[h] + 1
     
    return k
  
  
N = 701
c = 10**-2
D = 1000000
l = 0
m = 1

r0 = range(60, 700 , 1)

#k0 = k_SHO(N, c, D, l, m)

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
    k0 = k_SHO(N, c, D, l, m)
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


N = 6901
c = 10**-3
D = 100000

r0 = range(800, 6900 , 1)


mean = 0
lambdas = []
sd = []
variance = 0
p = 0


for i in range(10):
    k0 = k_SHO(N, c, D, l, m)
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

