import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

nums= list(map(int,input().split()))

nums.sort()

temp_1 = nums[0] + nums[5]
temp_2 = nums[1] + nums[4]
temp_3 = nums[2] + nums[3]


print(abs(max(temp_1,temp_2,temp_3) - min(temp_1,temp_2,temp_3)))