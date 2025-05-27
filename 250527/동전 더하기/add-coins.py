n, k = map(int,input().split())

coins = [int(input()) for _ in range(n)]

coins.sort(reverse = True)

ans = 0
cnt_sum = 0

for i in range(n):
    while True:
        if cnt_sum + coins[i] > k:
            break
        cnt_sum += coins[i]
        ans += 1
        #print(cnt_sum,coins[i],ans)

print(ans)




