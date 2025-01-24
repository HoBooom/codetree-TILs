n = int(input())
nums = list(map(int, input().split()))

# Write your code here!

templist=[]
anslist = []

nums.sort()

for i in range(n):
    templist.append((nums[i],nums[2*n - 1 - i]))
    anslist.append(nums[i] + nums[2*n - 1 - i])

print(max(anslist))
