from numpy import polyfit, zeros, log

from math import sqrt

from random import randrange

import matplotlib.pyplot as plt

import time

t0 = time.clock()

def ISW_3D(N, J, D, l):
    
    k = zeros(N)
    
    for i in range(D):
        j = zeros(3)
        n = 0
        
        while -J/(l[0]+1) < j[0] < J/(l[0]+1) and -J/(l[1]+1) < j[1] < J/(l[1]+1) and -J/(l[2]+1) < j[2] < J/(l[2]+1) and  n < N:
            
            a = randrange(-1, 2, 2)
            b = randrange(0, 2, 1)
            
            j[b] = j[b] + a
            n = n + 1         
        
        for h in range(n):
            k[h] = k[h] + 1
            
    return k

N = 3801
J = 32
D = 10000
l = [0, 0, 0]

r0 = range(600, 3800, 1)

#k0 = ISW_3D(N, J, D, l)

mean = 0
lambdas = []
sd = []
variance = 0
p = 0


for i in range(10):
    k0 = ISW_3D(N, J, D, l)
    p = -polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J
    lambdas.append(p)
    print p, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J)
    mean = ((len(lambdas) -1) * mean + p)/len(lambdas)
    

for i in lambdas:
    variance += ((mean - i)**2)/len(lambdas)
  
stddev = sqrt(variance)


print mean, stddev

#for o in range(0, 40, 5):
#    for p in range(150, 350, 5):
#        r0 = range(o, p, 1)
#        print o, p, (-polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J))


#plt.plot(r0, log([k0[i] for i in r0]))

#plt.plot(log(k0))
#plt . xlabel ('n')
#plt . ylabel ('ln(k)')
#plt . title ('J = 8, N = 100, D = 10000')

#plt.savefig('1DISW_N100J8D10000.png', bbox_inches='tight')

t1 = ((time.clock() - t0))
print t1



N = 1801
l = [1, 0, 0]

r0 = range(300, 1800, 1)

mean = 0
lambdas = []
sd = []
variance = 0
p = 0


for i in range(10):
    k0 = ISW_3D(N, J, D, l)
    p = -polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J
    lambdas.append(p)
    print p, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J)
    mean = ((len(lambdas) -1) * mean + p)/len(lambdas)
    

for i in lambdas:
    variance += ((mean - i)**2)/len(lambdas)
  
stddev = sqrt(variance)


print mean, stddev

t2 = ((time.clock() - t0 - t1))
print t2


N = 1051
l = [1, 1, 0]

r0 = range(150, 1050, 1)

mean = 0
lambdas = []
sd = []
variance = 0
p = 0


for i in range(10):
    k0 = ISW_3D(N, J, D, l)
    p = -polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J
    lambdas.append(p)
    print p, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J)
    mean = ((len(lambdas) -1) * mean + p)/len(lambdas)
    

for i in lambdas:
    variance += ((mean - i)**2)/len(lambdas)
  
stddev = sqrt(variance)


print mean, stddev

t3 = ((time.clock() - t0 - t1 - t2))
print t3




N = 1051
l = [1, 1, 1]

r0 = range(150, 1050, 1)

mean = 0
lambdas = []
sd = []
variance = 0
p = 0


for i in range(10):
    k0 = ISW_3D(N, J, D, l)
    p = -polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J
    lambdas.append(p)
    print p, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J)
    mean = ((len(lambdas) -1) * mean + p)/len(lambdas)
    

for i in lambdas:
    variance += ((mean - i)**2)/len(lambdas)
  
stddev = sqrt(variance)


print mean, stddev

t4 = ((time.clock() - t0 - t1 - t2 - t3))
print t2





N = 701
l = [2, 0, 0]

r0 = range(120, 700, 1)

mean = 0
lambdas = []
sd = []
variance = 0
p = 0


for i in range(10):
    k0 = ISW_3D(N, J, D, l)
    p = -polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=False)[0]*J*J
    lambdas.append(p)
    print p, sqrt(polyfit(r0, log([k0[i] for i in r0]), 1, rcond=None, full=False, w=None, cov=True)[1][0,0]*J*J)
    mean = ((len(lambdas) -1) * mean + p)/len(lambdas)
    

for i in lambdas:
    variance += ((mean - i)**2)/len(lambdas)
  
stddev = sqrt(variance)


print mean, stddev

t5 = ((time.clock() - t0 - t1 - t2 - t3 - t4))
print t5