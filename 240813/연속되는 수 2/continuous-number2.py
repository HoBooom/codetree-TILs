n = int(input())

max_fre = 0
nums= []

count = 0

for i in range(n):
    n = int(input())
    nums.append(n)
    if i == 0 or nums[i] != nums[i - 1]:
        if count > max_fre:
            max_fre = count
        count = 0
    count += 1
    
print(max_fre)