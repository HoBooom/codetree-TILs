n,m = map(int,input().split())

nums = []


def choose(cnt_n, cnt):
    if cnt_n == n + 1:
        if cnt == m:    
            print(*nums)
        return
    
    nums.append(cnt_n)
    choose(cnt_n + 1, cnt + 1)
    nums.pop()

    choose(cnt_n + 1, cnt)


choose(cnt_n = 1, cnt = 0)