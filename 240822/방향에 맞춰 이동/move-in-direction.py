n = int(input())

x = y = 0

for _ in range(n):
    c,m = input().split()
    m = int(m)
    if c== "N":
        y += m
    elif c=="S":
        y -= m
    elif c=="E":
        x += m
    elif c=="W":
        x -= m

print(x,y)