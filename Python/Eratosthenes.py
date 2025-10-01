from time import time
import numba as nb
st=time()
N=5*10**8
@nb.njit
def Primes1_to_N(N): #Eratosthenes
    sievelimit=int(N**.5)
    spf=[k for k in range(N+1)]
    for n in range(2,N+1):
        if n%2==0:
            spf[n]=2
        else: spf[n]=n
    for n in range(3,sievelimit+1,2):
        if spf[n]==n:
            for m in range(n**2, N + 1, 2*n):
                if spf[m]==m:
                    spf[m]=n
    return [p for p in range(2,N+1) if spf[p]==p]
P=Primes1_to_N(N)
print(time()-st)
