n,m = map(int,input().split())

a = []
b = []

a.append(0)
b.append(0)



cnt = 0
for _ in range(n):
    d,t = tuple(input().split())
    t = int(t)
    temp = a[cnt]
    if d =="R":
        for i in range(1,t + 1):
            a.append(temp + i)
            cnt += 1
    elif d =="L":
        for i in range(1,t + 1):
            a.append(temp - i)
            cnt += 1
    
    

cnt = 0

for _ in range(m):
    d,t = tuple(input().split())
    t = int(t)
    temp = b[cnt]
    if d =="R":
        for i in range(1,t + 1):
            b.append(temp + i)
            cnt += 1
    elif d =="L":
        for i in range(1,t + 1):
            b.append(temp - i)
            cnt += 1

ans = -1

for time in range(1,cnt):
    if a[time] == b[time]:
        ans = time
        break
print(ans)