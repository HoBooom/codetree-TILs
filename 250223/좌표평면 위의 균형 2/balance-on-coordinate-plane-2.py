import sys

MAXSIZE = sys.maxsize

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans = MAXSIZE

# Write your code here!
def line_f(x,y):
    for point in points:
        if point[0] == x or point[1] == y:
            return False
    return True

def count1(x,y):
    count = 0
    for point in points:
        if point[0] > x and point[1] > y:
            count +=1
    return count

def count2(x,y):
    count = 0
    for point in points:
        if point[0] < x and point[1] > y:
            count +=1
    return count

def count3(x,y):
    count = 0
    for point in points:
        if point[0] < x and point[1] < y:
            count +=1
    return count

def count4(x,y):
    count = 0
    for point in points:
        if point[0] > x and point[1] < y:
            count +=1
    return count




for x in range(1,101):
    for y in range(1,101):
        if line_f(x,y):
            count = []
            count.append(count1(x,y))
            count.append(count2(x,y))
            count.append(count3(x,y))
            count.append(count4(x,y))
            ans = min(max(count),ans)

print(ans)



        
