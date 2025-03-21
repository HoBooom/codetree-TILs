n = int(input())
nums = list(map(int,input().split()))

for i in range(n):
    cnt_max = 0
    cnt_max_idx = -1
    for j in range(n - i):
        if nums[j] > cnt_max:
            cnt_max = nums[j]
            cnt_max_idx = j
    nums[n - i - 1],nums[cnt_max_idx] = nums[cnt_max_idx],nums[n - i - 1]

print(*nums)

