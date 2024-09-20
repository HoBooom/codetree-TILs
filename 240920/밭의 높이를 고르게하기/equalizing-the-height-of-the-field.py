import sys

INT_MAX = sys.maxsize

n,h,t = map(int,input().split())
area = list(map(int,input().split()))
area.sort()

cost = INT_MAX


def check(area):
    temp = 0
    for i,v in enumerate(area):
        if v == h:
            temp += 1
    return temp

for i in range(n - t):
    temp = 0
    for j in range(i,i + t):
        temp += abs(area[j] - h)
    cost=min(cost,temp)

print(cost)