from multiset import Multiset
from sympy import factorint

A=Multiset(factorint(2**5*3**7*5**9))
B=Multiset(factorint(2**3*3**9))
print(A)
print(B)
print(A&B) #factorization of gcd of the numbers
print(A|B) #factorization of lcm of the numbers 
