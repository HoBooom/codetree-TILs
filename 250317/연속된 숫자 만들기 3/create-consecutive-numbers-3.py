nums = list(map(int,input().split()))

def is_end(nums):
    a,b,c = nums[0],nums[1],nums[2]
    return c-b == 1 and b-a == 1

count = 0

while True:
    if is_end(nums):
        break
    if nums[1] - nums[0] >= nums[2] - nums[1]:
        nums[2] = nums[1] - 1
        count += 1
    else:
        num[0] = nums[1] + 1
        count += 1
    nums.sort()
print(count)
    