n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
nums.sort()

def f(nums):
    for i,item in enumerate(nums):
        print(item,end=" ")
    print()

f(nums)
nums=reversed(nums)
f(nums)