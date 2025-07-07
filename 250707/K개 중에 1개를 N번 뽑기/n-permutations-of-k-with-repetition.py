K, N = map(int,input().split())

nums = []

def make_num(n):
    if n == N + 1:
        print(*nums)
        return
    
    for i in range(1,K + 1):
        nums.append(i)
        make_num(n + 1)
        nums.pop()

make_num(1)