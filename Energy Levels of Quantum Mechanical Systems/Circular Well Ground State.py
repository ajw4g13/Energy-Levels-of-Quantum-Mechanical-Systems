from math import sqrt

from random import randrange

from numpy import *

import matplotlib.pyplot as plt


def k_ground(N, J, D):
    
    k = zeros(N)
    
    for i in range(D):
        j = zeros(2)
        n = 0
        
        while linalg.norm(j, ord=None, axis=None, keepdims=False) < J and n < N:
            
            a = randrange(-1, 2, 2)            
            b = randrange(0, 2, 1)
            
            j[b] = j[b] + a
            n = n + 1
            
        for h in range(n):
            k[h] = k[h] + 1
            
    return k


N = 2000
J = 20
D = 10000

r0 = range(30, N, 1)

k0 = k_ground(N, J, D)
#k0 = [k0[i] for i in range(2J, N, 1)]
#p = polyfit(range(N), log(k), 1, rcond=None, full=False, w=None, cov=False)


print 'Ground State Energy:'
print '{0:<20} {1:<10}'.format("Mean lambda", "Standard Deviation:")
print '{0:<20} {1:<10}'.format(-polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J))

plt.plot(log(k0))
