n = int(input())

max_fre = 0
nums= []

count = 0

for i in range(n):
    n = int(input())
    nums.append(n)
    count += 1
    if count > max_fre:
            max_fre = count
    if i == 0 or nums[i] != nums[i - 1]:
        count = 0
    



print(max_fre)