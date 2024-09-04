import sys

INT_MIN = -sys.maxsize

n = int(input())

nums = list(map(int,input().split()))

ans = INT_MIN

for i in range(n-2):
    for j in range(i+2,n):
        temp = nums[i] + nums[j]
        ans = max(ans,temp)

print(ans)