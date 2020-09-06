def summer_69(list):
    flag = True
    sum_ = 0
    for i in list:
        if(flag == False):
            if(i == 9):
                flag = True
        elif(i == 6):
            flag = False
        else:
            sum_ += i
    return sum_
t=int(input())
while(t>0):
    t-=1
    num_array = []
    a= int(input("Enter how many elements you want:"))
    for i in range(a):
        n = int(input("num :"))
        num_array.append(int(n))

    print("summer_69", "[(",num_array,")]", "-->",summer_69(num_array))


