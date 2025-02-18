n = int(input())

lines = [tuple(map(int,input().split())) for _ in range(n)]

def is_on(a0,a1,b0,b1):
    if a0 < b0:
        if a1 > b1:
            return True
    elif a0 > b0:
        if a1 < b1:
            return True
    return False

on = 0

isnotline = [True]*n

for i in range(n - 1):
    a0,a1 = lines[i]
    for j in range(i+1,n):
        b0,b1 = lines[j]
        if is_on(a0,a1,b0,b1):
            on += 1
            #print(f'line ({a0},0)({a1},1) and line({b0},0)({b1},1)')
            isnotline[i] = False
            isnotline[j] = False

ans = 0
for i in range(n):
    if isnotline[i]:
        ans += 1


print(ans)
        

