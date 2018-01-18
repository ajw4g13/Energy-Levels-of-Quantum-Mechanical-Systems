from numpy import polyfit, zeros, log

from math import sqrt

from random import randrange

import matplotlib.pyplot as plt

import time

t0 = time.clock()

def ISW_1D(N, J, D, l, m):
    
    k = zeros(N)
    
    for i in range(D):
        j = 0
        n = 0
        
        while -J/(l+1) < j < J/(l+1) and n < N:
            
            a = randrange(-1, 2, 2)
            
            j = j + a
            n = n + 1         
        
        for h in range(n):
            k[h] = k[h] + 1
     
    return k

N = 100
J = 8
D = 10000
l = 0
m = 1

r0 = range(300, 2200, 1)

#k0 = ISW_1D(N, J, D, l, m)

#print 'Ground State Energy:'
#print '{0:<20} {1:<10}'.format("Mean lambda", "Standard Deviation:")
#print '{0:<20} {1:<10}'.format(-polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J))


mean = 0
lambdas = []
sd = []
variance = 0
p = 0


for i in range(10):
    k0 = ISW_1D(N, J, D, l, m)
    p = -polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J
    lambdas.append(p)
    print p, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J)
    mean = ((len(lambdas) -1) * mean + p)/len(lambdas)
    

for i in lambdas:
    variance += ((mean - i)**2)/len(lambdas)
   
stddev = sqrt(variance)


print mean, stddev

#for o in range(0, 40, 5):
 #   for p in range(150, 350, 5):
  #      r0 = range(o, p, 1)
   #     print o, p, (-polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J))


#print 'Expected lambda*J^2: ', pi*pi/8

#print 'Ground State Energy:'
#print '{0:<20} {1:<10}'.format("Mean lambda*J^2", "Standard Deviation:")
#print '{0:<20} {1:<10}'.format(-polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J))

#plt.plot(r0, log([k0[i] for i in r0]))

plt.plot(log(k0))
#plt . xlabel ('n')
#plt . ylabel ('ln(k)')
#plt . title ('J = 8, N = 100, D = 10000')



#40 100 1100 (4.8912967576018715, 5.3259280004646e-05)

#plt.savefig('1DISW_N100J8D10000.png', bbox_inches='tight')

#p = raw_input('Press any key to exit.')

##

t1 = ((time.clock() - t0))
print t1


