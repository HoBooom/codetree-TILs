n = int(input())

nums = list(map(int,input().split()))

ans = 0

for i in range(n):
    for j in range(i,n):
        temp_nums  = []
        nums_sum = 0
        for k in range(i,j + 1):
            nums_sum += nums[k]
            temp_nums.append(nums[k])
        mean = nums_sum / (j + 1 - i)
        #print(mean,temp_nums, j - i + 1)
        if mean in temp_nums:
            ans += 1

print(ans)