n=int(input("Input a number "))
d = dict()

for x in range(2,n+1,1):
    c=0
    for i in range(1,x+1,1):
        if (x % i) == 0:
            c=c+1
    if c==2 :
       d[x]=" prime"
    else :
        d[x]=" not prime"
print(d)
