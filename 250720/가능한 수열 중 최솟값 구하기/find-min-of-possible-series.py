n = int(input())

# nums_list = []

nums = []
found = False

def check():
    len_n = len(nums)
    for i in range(1,len_n + 1):
        for j in range(len_n - 2 * i + 1):
            if nums[j:j + i] == nums[j + i:j + 2 * i]:
                return False
    return True

def make_nums():
    if len(nums) == n:
        print(*nums, sep="")
        return True
    
    
        
    # global nums
    # global found
    # if found:
    #     return True

    # if len_n == n:
    #     if check(nums):
    #         print(*nums,sep="")
    #         found = True
    #         # nums_list.append(nums[:])
    #     return
    
    for i in range(4, 6 + 1):
        nums.append(i)
        if check():
            if make_nums():
                return True
        nums.pop()
    return False

make_nums()

# nums_list.sort()
# print(*nums_list[0],sep="")