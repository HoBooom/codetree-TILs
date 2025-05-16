n, m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def check(r,c,k):
    temp_count = 0
    for cnt_r in range(n):
        for cnt_c in range(n):
            if abs(r - cnt_r) + abs(c - cnt_c) <= k:
                temp_count += board[cnt_r][cnt_c]
    return temp_count

def cost(k):
    return k ** 2 + (k + 1) ** 2

ans = 0 

for r in range(n):
    for c in range(n):
        for k in range(2*(n-1)):
            cnt_benefit = check(r,c,k)
            cnt_cost = cost(k)
            if cnt_benefit * m >= cnt_cost:
                ans = max(cnt_benefit,ans)
            #print(f"r,c : {r},{c}  {cnt_benefit},{cnt_cost},{cnt_total}")
            

print(ans)


            
