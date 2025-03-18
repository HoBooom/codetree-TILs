n = int(input())

nums = list(map(int,input().split()))
nums.sort()

neg_nums = []
pos_nums = []

for i in range(n):
    if nums[i] > 0:
        pos_nums.append(nums[i])
    elif nums[i] < 0:
        neg_nums.append(nums[i])

ans = 0

if len(neg_nums) >= 2:
    if len(pos_nums) >= 3:
        t1 = pos_nums[-1] * pos_nums[-2] * pos_nums[-3]
        t2 = neg_nums[0] * neg_nums[1] * pos_nums[-1]
        ans = max(t1,t2)
    else:
        ans = pos_nums[-1] * pos_nums[-2] * pos_nums[-3]
else:
    if len(pos_nums) >= 3:
        ans = pos_nums[-1] * pos_nums[-2] * pos_nums[-3]
    else:
        ans = pos_nums[-1] * pos_nums[-2] * neg_nums[0]
print(ans)

