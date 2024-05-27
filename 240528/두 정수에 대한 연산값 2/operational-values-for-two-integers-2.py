def f1(a,b):
    if a > b:
        small = b + 10
        big = a * 2
        return small, big
    else:
        small = a + 10
        big  = b * 2
        return small, big


a,b = map(int,input().split())

s,b = f1(a,b)

print(s,b)