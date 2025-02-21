x0,x1 = map(int,input().split())

def f(n):
    ori = n
    temp = reversed(list(str(n)))
    temp = ''.join(temp)
    temp = int(temp)
    if ori == temp:
        return True
    return False

ans = 0

for i in range(x0,x1 + 1):
    if f(i):
        ans += 1
print(ans)