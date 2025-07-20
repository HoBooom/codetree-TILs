import sys

INT_MAX = sys.maxsize

n = int(input())

nums = list(map(int,input().split()))

ans = INT_MAX
not_found = True

def jump(cnt_pos,count):
    global ans
    global not_found
    
    if cnt_pos == n - 1:
        ans = min(ans,count)
        not_found = False
        return
    if nums[cnt_pos] == 0:
        return
    
    for i in range(1,nums[cnt_pos] + 1):
        n_pos = cnt_pos + i
        if n_pos <= n - 1:
            jump(n_pos, count + 1)
            not_jump = False


jump(cnt_pos = 0, count = 0)
if not_found:
    ans = -1

print(ans)

    

