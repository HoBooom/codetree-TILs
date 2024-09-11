import sys

INT_MAX = sys.maxsize

ans = INT_MAX


n,s = map(int,input().split())

nums = list(map(int,input().split()))

for i in range(n - 1):
    for j in range(i + 1,n):
        n1,n2 = nums[i],nums[j]
        nums[i],nums[j] = 0,0
        sum_nums = sum(nums)
        nums[i],nums[j] = n1,n2
        ans = min(ans,abs(s - sum_nums))
        
print(ans)