import sys

nums = list(map(int,input().split()))

if nums[2] - nums[1] == nums[1] - nums[0] == 1:
    print(0)
    sys.exit()

max_move = 0

max_move = max(max_move,nums[2] - nums[1] - 1)
max_move = max(max_move,nums[1] - nums[0] - 1)

print(max_move)