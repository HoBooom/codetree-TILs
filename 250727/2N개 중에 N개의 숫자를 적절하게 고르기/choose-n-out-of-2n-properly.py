import sys

INT_MAX = sys.maxsize

n = int(input())

nums = list(map(int,input().split()))

a_nums = []

ans = INT_MAX


def calc():
    a_sum = sum(a_nums)
    b_sum = (sum(nums) - a_sum)
    return abs(a_sum - b_sum)


def choose(cur_idx, cnt):
    global ans
    if cnt == n:
        cal_c = calc()
        ans = min(ans, calc())
        # if ans > cal_c:
        #     print(a_nums, cal_c)
        #     ans = cal_c
    
    if cur_idx == 2 * n:
        return

    choose(cur_idx + 1, cnt)
    a_nums.append(nums[cur_idx])

    choose(cur_idx + 1, cnt + 1)
    a_nums.pop()

choose(0,0)

print(ans)