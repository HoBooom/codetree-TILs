import sys

INT_MAX = sys.maxsize

n = int(input())

point = []

for _ in range(n):
    x,y = map(int,input().split())
    point.append((x,y))

ans_min = INT_MAX

def dis(points):
    temp = 0
    for i in range(len(points) - 1):
        x0,y0 = points[i][0], points[i][1]
        x1,y1 = points[i+1][0], points[i+1][1]
        distance = abs(x0 - x1) + abs(y0 - y1)
        #print(f"x0: {x0}, x1: {x1}")
        #print(f"y0: {y0}, y1: {y1}")
        temp += distance
    #print(temp)
    return temp

for i in range(1,n - 1):
    temp_point = point.pop(i)
    temp_ans = dis(point)
    ans_min = min(temp_ans,ans_min)
    point.insert(i,temp_point)

print(ans_min)