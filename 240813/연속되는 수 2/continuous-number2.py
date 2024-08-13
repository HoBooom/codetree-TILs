n = int(input())

max_fre = 0
nums= []

count = 0

for i in range(n):
    n = int(input())
    nums.append(n)
    count += 1
    if i == 0 or nums[i] != nums[i - 1]:
        if count > max_fre:
            max_fre = count
        count = 0
    
if n > 0 and max_fre == 0:
    if count == 1:
        max_fre = 1
    else:
        max_fre = count


print(max_fre)