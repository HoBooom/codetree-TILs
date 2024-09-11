import sys

INT_MIN = - sys.maxsize

ans = INT_MIN

n,k = map(int,input().split())
nums = list(map(int,input().split()))

for i in range(n - k + 1):
    temp = sum(nums[i:i+k])
    #print(nums[i:i+k])
    ans = max(ans,temp)

print(ans)