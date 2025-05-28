n = int(input())

times = [tuple(map(int,input().split())) for _ in range(n)]

times.sort(key = lambda x : x[1])

ans = 1

cnt_time = times[0]

for i in range(1,n):
    if cnt_time[1] <= times[i][0]:
        ans += 1
        cnt_time = times[i]

print(ans)