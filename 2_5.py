def list1(num):
    mum = 1
    for x in num:
        mum = mum*int(x)
    return mum
num = ["1","4","6","10"]
num2 = list1(num)
num2 = int(num2)
print(num2)