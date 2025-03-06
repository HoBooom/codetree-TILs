import sys

MAXINT = sys.maxsize

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]


# Write your code here!

def distance(points):
    dis = 0
    for i in range(len(points) - 1):
        dis += abs(points[i][0] - points[i + 1][0]) + abs(points[i][1] - points[i + 1][1])
    return dis

ans = MAXINT

for i in range(1,len(points) - 1):
    cnt_dis = distance(points[:i] + points[i + 1:])
    ans = min(ans,cnt_dis)

print(ans)