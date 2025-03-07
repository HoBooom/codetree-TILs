n = int(input())
order = [tuple(map(int,input().split())) for _ in range(n)]
time = [0] * 1001

for _,(a,b) in enumerate(order):
    for i in range(a,b):
        time[i] += 1

ans = 0

for i in range(n):
    cnt_time = 0
    a,b = order[i]
    for j in range(a,b + 1):
        time[j] -= 1
    cnt_time = sum(time) 
    ans = max(ans,cnt_time)
    for j in range(a,b + 1):
        time[j] += 1

print(ans)
