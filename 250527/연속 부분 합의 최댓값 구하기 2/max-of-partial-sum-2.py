import sys

INT_MIN = -sys.maxsize

n = int(input())

nums = list(map(int,input().split()))

ans = INT_MIN
cnt_sum = 0

for i in range(n):
    cnt_sum += nums[i]
    ans = max(cnt_sum,ans)

    if cnt_sum < 0:
        cnt_sum = 0
    #print(cnt_sum,ans)

print(ans)




