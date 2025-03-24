n = int(input())
nums = list(map(int,input().split()))

for i in range(1,n):
    cnt_num = nums[i] # i = 1
    j = i - 1 # j = 0
    while j >= 0 and nums[j] > cnt_num:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = cnt_num
print(*nums)

