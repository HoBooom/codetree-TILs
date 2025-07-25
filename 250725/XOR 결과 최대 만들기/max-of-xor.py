n, m = map(int,input().split())

nums = list(map(int,input().split()))

choosed_nums = []
xor_max = 0

def choose_nums(cnt_num, count_n):
    global xor_max

    if count_n == m:
        cnt_xor = 0
        for num in choosed_nums:
            cnt_xor ^= num
        #print(cnt_xor)
        xor_max = max(cnt_xor, xor_max)
        return
    
    if cnt_num == n:
        return
    
    choosed_nums.append(nums[cnt_num])
    choose_nums(cnt_num + 1, count_n + 1)
    choosed_nums.pop()

    choose_nums(cnt_num + 1, count_n)

choose_nums(0, 0)
print(xor_max)
