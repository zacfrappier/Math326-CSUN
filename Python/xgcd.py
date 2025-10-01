def xgcd(b,n):
    x0,x1,y0,y1=1,0,0,1
    print(' ',b,n,x0,x1,y0,y1)
    while n:
        q,b,n=b//n,n,b%n
        x0,x1=x1,x0-q*x1
        y0,y1=y1,y0-q*y1
        print(q,b,n,x0,x1,y0,y1)
    return b,x0,y0
print(xgcd(662,414))
