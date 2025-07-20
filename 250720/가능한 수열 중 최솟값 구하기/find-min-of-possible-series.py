n = int(input())

nums_list = []

nums = []

def check(num):
    for i in range(1,n + 1):
        for j in range(n - 2 * i + 1):
            if nums[j:j + i] == nums[j + i:j + 2 * i]:
                return False
    return True

def make_nums(len_n):
    global nums
    if len_n == n:
        if check(nums):
            #print(*nums)
            nums_list.append(nums[:])
        return
    
    for i in range(4, 6 + 1):
        nums.append(i)
        make_nums(len_n + 1)
        nums.pop()

make_nums(0)

nums_list.sort()
print(*nums_list[0],sep="")