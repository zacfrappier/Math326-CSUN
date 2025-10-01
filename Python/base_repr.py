def base_repr(n,b):
    ls=[]
    while n:
        ls.append(n%b)
        n//=b
    return ls
def base_repr_traditional(n,b):
    ls=base_repr(n,b)
    ls1=list(reversed(ls))
    s=''
    for d in ls1:
        s+=str(d)
    return s
