n = int(input())
order = [tuple(map(int,input().split())) for _ in range(n)]


ans = 0

for i in range(n):
    cnt_time = [0] * 1001
    cnt_order = order[:i] + order[i + 1:]
    for a,b in cnt_order:
        for j in range(a,b):
            cnt_time[j] = 1
    ans = max(ans,sum(cnt_time))

    
print(ans)
