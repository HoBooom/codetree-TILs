n = int(input())
nums = list(map(int,input().split()))

def check(num_list):
    for i in range(n-1):
        if num_list[i] > nums[i + 1]:
            return False
    return True


def shift_front(idx,num_list):
    temp_n = num_list[0]
    for i in range(1,idx + 1):
        num_list[i - 1] = num_list[i]
    num_list[idx] = temp_n

count = 0 
while True:
    if check(nums):
        break
    cnt_front = nums[0]
    for i in range(1,n):
        if nums[i] == cnt_front -1 or cnt_front == 1 and nums[i] == n:
            shift_front(i,nums)
            count += 1
            break
    
#     print(nums)
# print(*nums)
print(count)

