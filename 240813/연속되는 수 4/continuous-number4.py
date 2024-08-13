n = int(input())

length = 0

nums = []
count = 0

for i in range(n):
    num = int(input())
    nums.append(num)
    if i == 0  or nums[i] - nums[i - 1] <= 0:
        count = 0
    count += 1
    if length < count:
        length = count

print(length)