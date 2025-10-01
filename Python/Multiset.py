from multiset import Multiset
from collections import Counter
A=Multiset({1:3,2:2,3:5})
B=Multiset({1:2,2:5,3:5,4:2})
A1=Counter({1:3,2:2,3:5})
B1=Counter({1:2,2:5,3:5,4:2})
print('A=', A)
print('B=', B)
print('A1=',A1)
print(A==A1) #They work the same way but they are different data structure
print(A|B) #A union B
print(A&B) #A intersection B
print(A-B) #A set difference B
print(B-A) #B set difference A
print(A^B) #symmetric difference, (A-B) union (B-A)
print(A1|B1) #A union B
print(A1&B1) #A intersection B
print(A1-B1) #A set difference B
print(B1-A1) #B set difference A
#print(A1^B1) #symmetric difference, (A-B) union (B-A), not supported for Counter
print(list(A))
print(list(A1))
