def spy_game(list):
    flag = True
    sum_ = 0
    c=0
    for i in list:
        if(i == 0):
            c=c+1
        elif(i==7):
            sum_=sum_+1

    if(c == 2 and sum_==1):
        flag = True
    else:
            flag = False
    return flag
t=int(input())
while(t>0):
    t-=1
    num_array = []
    a= int(input("Enter how many elements you want:"))
    for i in range(a):
        n = int(input("num :"))
        num_array.append(int(n))

    print("spy_game", "(",num_array,")", "-->",spy_game(num_array))


