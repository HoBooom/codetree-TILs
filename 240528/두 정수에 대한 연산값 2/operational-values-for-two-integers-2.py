def f1(a,b):
    if a > b:
        return b + 10, a*2
    else:
        return a + 10,b*2


a,b = map(int,input().split())

s,b = f1(a,b)

print(s,b)