import sys

MAXSIZE = sys.maxsize

n = int(input())
A = list(map(int, input().split()))

# Write your code here!

def distance(a,b):
    return abs(a - b)

ans = MAXSIZE

for i in range(n):
    dis = 0
    for home in range(n):
        dis += distance(home,i)*A[home]
    if dis < ans:
        ans = dis

print(ans)
        
