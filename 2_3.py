a=input("enter the string: ")
count1=0
count2=0
for i in a:
    if i.islower():
        count1=count1+1
    elif i.isupper():
        count2=count2+1

print("upper case letters are :",count2)
print("lower case letters are :",count1)