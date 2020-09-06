def oddeven(a,b):
     if a%2==0 and b%2==0:
         if(a<b):
             return a
         else:
             return b
     else:
         if(a>b):
             return a
         else:
             return b



a= int(input())
b=int(input())

print ("lesser_of_two_evens (",a,",",b,")"," -->",oddeven(a,b))
