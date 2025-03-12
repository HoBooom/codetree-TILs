n, k = map(int,input().split())

nums = list(map(int,input().split()))

nums.sort()

cnt_min = nums[0]
cnt_max = nums[-1]

def min_num_count(nums):
    count = 1
    for i in range(n - 1):
        if nums[i] != nums[i + 1]:
            break
        count += 1
    return count

def max_num_count(nums):
    count = 1
    for i in reversed(range(1,n)):
        if nums[i] != nums[i - 1]:
            break
        count += 1
    return count

cnt_cost = 0

while cnt_max - cnt_min > k:
    max_minus_cost = max_num_count(nums)
    min_plus_cost = min_num_count(nums)
    if max_minus_cost > min_plus_cost:
        for i in range(n):
            if nums[i] == cnt_min:
                nums[i] += 1
        cnt_cost += min_plus_cost
    else:
        for i in reversed(range(n)):
            if nums[i] == cnt_max:
                nums[i] -= 1
        cnt_cost += max_minus_cost
    # print(f"cnt_max {cnt_max},{max_minus_cost} cnt_min {cnt_min},{min_plus_cost} cnt_cost {cnt_cost}")
    # print(*nums)
    cnt_max = nums[-1]
    cnt_min = nums[0]

print(cnt_cost)
    
                
