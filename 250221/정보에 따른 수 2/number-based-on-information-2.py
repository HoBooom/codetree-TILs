import sys

MAXSIZE = sys.maxsize

t,a,b = map(int,input().split())

s = []
n = []

for _ in range(t):
    alpha, pos = input().split()
    if alpha == 'S':
        s.append(int(pos))
    elif alpha == 'N':
        n.append(int(pos))

def min_s(x0):
    dis = MAXSIZE
    for _,item in enumerate(s):
        temp = abs(x0 - item)
        if temp < dis:
            dis = temp
    return dis

def min_n(x0):
    dis = MAXSIZE
    for _,item in enumerate(n):
        temp = abs(x0 - item)
        if temp < dis:
            dis = temp
    return dis

ans = 0

for i in range(a,b + 1):
    if min_n(i) >= min_s(i):
        ans += 1

print(ans)