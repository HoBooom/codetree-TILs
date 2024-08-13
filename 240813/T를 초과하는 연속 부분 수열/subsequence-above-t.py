n,t = map(int,input().split())

length = 0
max_len = 0

nums = list(map(int,input().split()))

for i in range(n):
    if nums[i] > t:
        length += 1
    elif nums[i] <= t:
        length = 0
        
    if length > max_len:
        max_len = length

print(max_len)