from numpy import polyfit, zeros, log

from math import sqrt

from random import randrange

import matplotlib.pyplot as plt

import time

t0 = time.clock()

def k_ISW(N, J, D, l, m, d):
    
    k = zeros(N)
    
    for i in range(D):
        j = zeros(d)
        n = 0
        
        while linalg.norm(j, ord=None, axis=None, keepdims=False) < J/(l+1) and n < N:
            
            a = randrange(-1, 2, 2)
            
            j = j + a
            n = n + 1         
        
        for h in range(n):
            k[h] = k[h] + 1
     
    return k

N = 22000
J = 32
D = 10000
l = 0
m = 1

r0 = range(300, 2200, 1)

k0 = k_ISW(N, J, D, l, m)

#mean = 0
#lambdas = []
#sd = []
#variance = 0
#p = 0


#for i in range(10):
#    k0 = k_ISW(N, J, D, l, m)
#    p = -polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J
#    lambdas.append(p)
#    print p, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J)
#    mean = ((len(lambdas) -1) * mean + p)/len(lambdas)
    

#for i in lambdas:
#    variance += ((mean - i)**2)/len(lambdas)
   
#stddev = sqrt(variance)


#print mean, stddev

#for o in range(0, 40, 5):
 #   for p in range(150, 350, 5):
  #      r0 = range(o, p, 1)
   #     print o, p, (-polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J))


#plt.plot(r0, log([k0[i] for i in r0]))

plt.plot(log(k0))
#plt . xlabel ('n')
#plt . ylabel ('ln(k)')
#plt . title ('J = 8, N = 100, D = 10000')

#plt.savefig('1DISW_N100J8D10000.png', bbox_inches='tight')

t1 = ((time.clock() - t0))
print t1
