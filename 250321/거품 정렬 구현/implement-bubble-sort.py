n = int(input())
nums = list(map(int,input().split()))

for i in range(n):
    for j in range(n - i - 1):
        if nums[j + 1] < nums[j]:
            nums[j + 1],nums[j] = nums[j],nums[j + 1]

print(*nums)