n,m = map(int,input().split())

a = []
b = []
forward = 0
a.append(0)
b.append(0)


cnt = 0
for _ in range(n):
    v,t = map(int,input().split())
    
    for time in range(t):
        cnt += v
        a.append(cnt)

cnt = 0
for _ in range(m):
    v,t = map(int,input().split())
    
    for time in range(t):
        cnt += v
        b.append(cnt)

change = 0

for i in range(1,len(a)):
    if forward == 0:
        if a[i] > b[i]:
            forward = 1
        elif a[i] < b[i]:
            forward = 2
        else:
            continue
    if forward == 1:
        if a[i] < b[i]:
            change += 1
            forward = 2
    elif forward == 2:
        if a[i] > b[i]:
            change += 1
            forward = 1

print(change)