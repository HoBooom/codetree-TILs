x,y = map(int,input().split())

def f(n):
    n = str(n)
    n = list(n)
    num_list = [0]*10

    for i in range(len(n)):
        num_list[int(n[i])] += 1
    count = 0
    for i in range(len(num_list)):
        if num_list[i] >= 1:
            count += 1
    #print(num_list)
    if count >= 3:
        return False
    if count == 2:
        t = 0
        for i in range(len(num_list)):
            if num_list[i] >= 2:
                t += 1
        if t == 2:
            return False
        elif t == 1:
            return True
    return False

ans = 0
for i in range(x,y + 1):
    if f(i):
        ans += 1
print(ans)

