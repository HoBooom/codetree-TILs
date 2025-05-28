n = int(input())

nums = list(map(int,input().split()))


cost = 0
while True:
    if len(nums) == 1:
        break
    nums.sort()
    a = nums.pop(0)
    b = nums.pop(0)
    nums.append(a + b)
    cost += a + b

print(cost)

