from time import time
import numba as nb
st=time()
N=5*10**8
@nb.njit
def Primes2_to_N(N): 
    isprime = [1]*(N+1) #linear sieve
    isprime[0] = isprime[1] = 0
    P = []
    spf = [0]+[1]*N
    for i in range(2, N+1):
        if isprime[i]:
            P.append(i)
            spf[i] = i
        j = 0
        while (P[j] <= spf[i] and i*P[j] < N+1):
            isprime[i*P[j]] = 0
            spf[i*P[j]] = P[j]
            j += 1
            if j>=len(P): break
    return P
P=Primes2_to_N(N)
print(time()-st)
