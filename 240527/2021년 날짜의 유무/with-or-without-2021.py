def is_date(m,d):
    if m == 2 and d>28:
        return False
    elif m <=7 and m % 2 != 0:
        if d > 31:
            return False
    elif m <=7 and m % 2 ==0:
        if d > 30:
            return False
    elif m >7 and m % 2 ==0:
        if d > 31:
            return False
    elif m > 7 and m % 2!=0:
        if d > 30:
            return False
    return True









m,d = map(int,input().split())

tf = is_date(m,d)

if tf:
    print("Yes")
else:
    print("No")