lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())

    lst.append(ele)
if(n==3):
    print("has_33", "[(", lst , ")]", "--> True")
else:
    print("has_33", "[(", lst, ")]", "--> False")