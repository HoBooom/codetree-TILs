import sys

INT_MAX = sys.maxsize

n,h,t = map(int,input().split())
area = list(map(int,input().split()))

cost = INT_MAX

#print(area)
def check(area):
    temp = 0
    for i,v in enumerate(area):
        if v == h:
            temp += 1
    return temp

for i in range(n - t + 1):
    temp = 0
    for j in range(i,i + t):
        temp += abs(area[j] - h)
    #print(cost,temp)
    cost=min(cost,temp)

print(cost)