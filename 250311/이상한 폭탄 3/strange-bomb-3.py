n, k = map(int,input().split())

boom = [int(input()) for _ in range(n)]

max_n = -1
ans = 0

for i in range(n):
    start = 0
    if i - k < 0:
        start = 0
    else:
        start = i - k
    if i + k >= n:
        end = n - 1
    else:
        end = i + k
    cnt_boom = boom[i]
    for j in range(start,end + 1):
        count = 0
        temp = boom[j:j + k]
        for _,item in enumerate(temp):
            if item == cnt_boom:
                count += 1
        if max_n < count:
            ans = boom[i]
            max_n = count

print(ans)

    


