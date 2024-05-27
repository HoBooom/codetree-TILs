def f1(a,b):
    if a > b:
        small = b + 10
        big = a * 2
        return big, small
    else:
        small = a + 10
        big  = b * 2
        return small, big


a,b = map(int,input().split())

a,b = f1(a,b)


print(a,b)