def sum_p(a,b,c):
    sum=int(a+b+c)
    if(sum<21):
        return sum
    else:
        sum=sum-10
        if(sum<21):
            return sum
        else:
            return 0
t=int(input())
while(t>0):
    t-=1
    a=int(input())
    b=int(input())
    c=int(input())
    if(sum_p(a,b,c)==0):
        print("blackjack", "[(", a,b,c, ")]", "--> blast")
    else:
        print("blackjack", "[(", a, b, c, ")]", "-->",sum_p(a,b,c))