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


N = 100
J = 18
D = 1000

lambdas = []
mean2 = 0
variance = 0

for i in range(10):
    
    k2 = k_second(N, J, D)
#    p = polyfit(range(N), log(k), 1, rcond=None, full=False, w=None, cov=False)
    k2 = [k2[i + 2*J] for i in range(N - 2*J)]
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
