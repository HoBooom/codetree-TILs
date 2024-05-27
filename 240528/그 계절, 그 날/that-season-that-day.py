def is_yoon(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    elif y % 4 == 0 and y % 400 == 0: # 100으로 배수이지만 400으로 나눠짐
        return True
    return False


def season(m):
    if m >=3 and m <=5:
        return 0
    elif m >=6 and m <=8:
        return 1
    elif m >=9 and m <=11:
        return 2
    else:
        return 3

def is_31(m):
    month = [1,3,5,7,8,10,12]
    if m in month:
        return True
    else:
        return False



y,m,d = map(int,input().split())

if is_yoon(y):
    if m == 2 and d > 29:
        print(-1)
    elif not is_31(m) and d >30:
        print(-1)
    elif is_31:
        if season(m) == 0:
            print("Spring")
        elif season(m) ==1:
            print("Summer")
        elif season(m) ==2:
            print("Fall")
        elif season(m) ==3:
            print("Winter")
else:
    if m == 2 and d > 28:
        print(-1)
    elif not is_31(m) and d >30:
        print(-1)
    elif is_31:
        if season(m) == 0:
            print("Spring")
        elif season(m) ==1:
            print("Summer")
        elif season(m) ==2:
            print("Fall")
        elif season(m) ==3:
            print("Winter")