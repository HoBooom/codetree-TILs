MAX_INT = 10000

n,m = map(int,input().split())

arr = list(map(int,input().split()))

ans = MAX_INT

for i in range(1,MAX_INT):
    cnt_sum = 0
    section = 1

    is_ok = True
    for j in range(n):
        if arr[j] > i:
            is_ok = False
            break
        cnt_sum += arr[j]
        if cnt_sum > i:
            section += 1
            cnt_sum = arr[j]
    if section <= m and is_ok:
        ans = min(ans,i)

print(ans)

        

