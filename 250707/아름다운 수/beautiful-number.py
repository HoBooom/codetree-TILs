N = int(input())

count = 0
nums = []

def is_beautiful(nums):
    i = 0
    while i < len(nums):
        num = nums[i]
        if num > 4:
            return False
        for j in range(i,i + num):
            if nums[j] != num:
                return False
        i += num
    return True


def make_num(n):
    global count
    if n == N + 1:
        if is_beautiful(nums):
            count += 1
        #print(*nums)
        return
    elif n > N + 1:
        return

    for i in range(1,N + 1):
        for j in range(i):
            nums.append(i)
        make_num(n + i)
        for j in range(i):
            nums.pop()

make_num(1)
print(count)
        



