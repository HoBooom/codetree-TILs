import sys

n = int(input())

residents = list(map(int,input().split()))

INT_MIN = - sys.maxsize
INT_MAX = sys.maxsize

min_dis = INT_MAX


for i in range(n):
    temp_dis = 0
    for j in range(n):
        temp_dis += residents[j] * (abs(j - i))
    min_dis = min(temp_dis,min_dis)
    #print(temp_dis)

print(min_dis)