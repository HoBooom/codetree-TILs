import sys

INT_MAX = sys.maxsize
MAX_H = 100

n = int(input())
k = 17
hill = [int(input()) for _ in range(n)]

ans = INT_MAX

for i in range(MAX_H):
    cost = 0
    for j in range(n):
        if hill[j] < i:
            cost += (hill[j] - i) ** 2
        if hill[j] > i + k:
            cost += (hill[j] - (i + k)) ** 2
    ans = min(ans,cost)

print(ans)