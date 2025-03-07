x,y = map(int,input().split())

def f(n):
    n = list(str(n))
    num_list = [0]*10

    for i in range(len(n)):
        num_list[int(n[i])] += 1
    count = 0
    is_interesting = False
    for i in range(10):
        if num_list[i] == len(n) - 1:
            is_interesting = True
    return is_interesting

ans = 0
for i in range(x,y + 1):
    if f(i):
        ans += 1
print(ans)

