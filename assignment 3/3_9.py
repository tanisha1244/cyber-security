def near_hundred(n):
    p=0
    for i in range(2,n):
        c=0
        for k in range(2,i):
           if(i%k==0):
             break
           else:
               c=c+1
        if(c!=0):
            p=p+1
    return p
a=int(input())
print ( "count_primes","(",a,")","-->",near_hundred(a))