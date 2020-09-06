def near_hundred(n):
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        return True
    else:
        return False
a=int(input())
print ( "almost_there","(",a,")","-->",near_hundred(a))