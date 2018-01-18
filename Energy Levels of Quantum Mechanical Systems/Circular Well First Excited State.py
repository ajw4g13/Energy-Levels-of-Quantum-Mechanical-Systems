from random import randrange

from numpy import zeros, linalg


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


N = 2000
J = 20
D = 10000

#lambdas = []
#mean1 = 0
#variance = 0

#for i in range(10):
    
#    k1 = k_first(N, J, D)
#    p = polyfit(range(N), log(k), 1, rcond=None, full=False, w=None, cov=False)
#    k1 = [k1[i + 2*J] for i in range(N - 2*J)]
#    p = polyfit(range(2*J, N, 1), log(k1), 1, rcond=None, full=False, w=None, cov=False)
#    lambdas.append(-p[0])
#    mean1 = ((len(lambdas)-1)*mean1 -p[0])/len(lambdas)   

#for i in range(len(lambdas)):
#    variance += ((lambdas[i] - mean1)**2)/len(lambdas)                    

#standarddev1 = sqrt(variance)                            # Calculates standard deviation of critical mass.

#print 'First Excited State Energy:'
#print '{0:<20} {1:<10}'.format("Mean lambda*J^2", "Standard Deviation:")
#print '{0:<20} {1:<10}'.format(mean1*J*J, standarddev1*J*J)
