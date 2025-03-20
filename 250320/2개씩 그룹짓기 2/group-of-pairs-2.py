import sys
INT_MAX = sys.maxsize

n = int(input())
nums = list(map(int,input().split()))
nums.sort()

new_nums = []


for i in range(n):
    new_nums.append((nums[i],nums[n + i]))

ans = INT_MAX
for _,(n1,n2) in enumerate(new_nums):
    ans = min(ans,abs(n2 - n1))

print(ans)
