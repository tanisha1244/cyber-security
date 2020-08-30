def check(l,h,a):
    if a in range(l,h):
        return True
    else:
            return False
l=input()
l=int(l)
h=input()
h=int(h)
a=input()
a=int(a)
print(check(l,h,a))