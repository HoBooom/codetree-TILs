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
    temp_points = points[:]
    temp_points.pop(i)
    #print(temp_points,end = " ")
    cnt_dis = distance(temp_points)
    #print(cnt_dis)
    if ans > cnt_dis:
        ans = cnt_dis

print(ans)