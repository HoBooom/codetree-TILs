import sys

INT_MAX = sys.maxsize

n = int(input())

nums = list(map(int,input().split()))

a_nums = []
b_nums = []

ans = INT_MAX

def b_select():
    b_nums.clear()
    for num in nums:
        if num not in a_nums:
            b_nums.append(num)

def calc():
    return abs(sum(a_nums) - sum(b_nums))


def choose(cur_idx, cnt):
    global ans
    if cnt == n:
        b_select()
        #print(a_nums, b_nums)
        ans = min(ans, calc())
    
    if cur_idx == 2 * n:
        return

    choose(cur_idx + 1, cnt)
    a_nums.append(nums[cur_idx])

    choose(cur_idx + 1, cnt + 1)
    a_nums.pop()

choose(0,0)

print(ans)