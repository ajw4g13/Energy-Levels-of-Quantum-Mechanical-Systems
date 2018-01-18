from random import randrange

from numpy import *


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


N = 200
J = 30
D = 1000

lambdas = []
mean0 = 0
variance = 0

for i in range(10):
    
    k0r = k_ground(N, J, D)
#    p = polyfit(range(N), log(k), 1, rcond=None, full=False, w=None, cov=False)
    k0 = [k0r[i + 2*J] for i in range(N - 2*J)]
    p = polyfit(range(2*J, N, 1), log(k0), 1, rcond=None, full=False, w=None, cov=False)
    lambdas.append(-p[0])
    mean0 = ((len(lambdas)-1)*mean0 -p[0])/len(lambdas)   

for i in range(len(lambdas)):
    variance += ((lambdas[i] - mean0)**2)/len(lambdas)                    

standarddev0 = sqrt(variance)                            # Calculates standard deviation of critical mass.

print 'Ground State Energy:'
print '{0:<20} {1:<10}'.format("Mean lambda", "Standard Deviation:")
print '{0:<20} {1:<10}'.format(mean0*J*J, standarddev0*J*J)

def k_first(N, J, D):
    
    k = zeros(N)
    
    for i in range(D):
        j = [J/2, 0]
        n = 0
        
        while -J < linalg.norm(j, ord=None, axis=None, keepdims=False) < J and j[0] != 0 and n < N:
            
            a = randrange(-1, 2, 2)
            b = randrange(0, 2, 1)
            
            j[b] = j[b] + a

            n = n + 1
        
        for h in range(n):
            k[h] = k[h] + 1
     
    return k


lambdas = []
mean1 = 0
variance = 0

for i in range(10):
    
    k1r = k_first(N, J, D)
#    p = polyfit(range(N), log(k), 1, rcond=None, full=False, w=None, cov=False)
    k1 = [k1r[i + 2*J] for i in range(N - 2*J)]
    p = polyfit(range(2*J, N, 1), log(k1), 1, rcond=None, full=False, w=None, cov=False)
    lambdas.append(-p[0])
    mean1 = ((len(lambdas)-1)*mean1 -p[0])/len(lambdas)   

for i in range(len(lambdas)):
    variance += ((lambdas[i] - mean1)**2)/len(lambdas)                    

standarddev1 = sqrt(variance)                            # Calculates standard deviation of critical mass.

print 'First Excited State Energy:'
print '{0:<20} {1:<10}'.format("Mean lambda*J^2", "Standard Deviation:")
print '{0:<20} {1:<10}'.format(mean1*J*J, standarddev1*J*J)


from random import randrange

from numpy import *


def k_second(N, J, D):
    
    k = zeros(N)
  
    for i in range(D):
        j = [J/2, J/2]
        n = 0
        
        while linalg.norm(j, ord=None, axis=None, keepdims=False) < J and j[0] != 0 and j[1] != 0 and n < N:
            
            a = randrange(-1, 2, 2)
            b = randrange(0, 2, 1)
            
            j[b] = j[b] + a

            n = n + 1
            
        for h in range(n):
            k[h] = k[h] + 1
     
    return k


lambdas = []
mean2 = 0
variance = 0

for i in range(10):
    
    k2r = k_second(N, J, D)
#    p = polyfit(range(N), log(k), 1, rcond=None, full=False, w=None, cov=False)
    k2 = [k2r[i + 2*J] for i in range(N - 2*J)]
    p = polyfit(range(2*J, N, 1), log(k2), 1, rcond=None, full=False, w=None, cov=False)
    lambdas.append(-p[0])
    mean2 = ((len(lambdas)-1)*mean2 -p[0])/len(lambdas)   

print k2

for i in range(len(lambdas)):
    variance += ((lambdas[i] - mean2)**2)/len(lambdas)                    

standarddev2 = sqrt(variance)                            # Calculates standard deviation of critical mass.

print 'Second Excited State Energy:'
print '{0:<20} {1:<10}'.format("Mean J^2*lambda", "Standard Deviation:")
print '{0:<20} {1:<10}'.format(mean2*J*J, standarddev2*J*J)

print ' '

print 'G/F:', mean0*J*J/(mean1*J*J)
print 'G/S:', mean0*J*J/(mean2*J*J)
print 'F/S:', mean1*J*J/(mean2*J*J)