n=int(input("Input a number "))
d = []
for x in range(2,n+1,1):
    c=0
    for i in range(1,x+1,1):
        if (x % i) == 0:
            c=c+1
    if c==2 :
        list1=[int(x)]
        d.append((x,"prime"))

    else :
        list1=[int(x)]
        d.append((x,"not prime"))
print(d)
