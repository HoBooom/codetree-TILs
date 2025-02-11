import sys

MAXSIZE = sys.maxsize

n = int(input())
a = [int(input()) for _ in range(n)]

# Write your code here!

def dis(a,b):#a->b
    if b > a:
        return b - a
    elif b == a:
        return 0
    else:
        return (n - a) + b

ans = MAXSIZE

for i in range(n):
    temp_dis = 0
    for j in range(n):
        temp_dis += dis(i,j) * a[j]
    if temp_dis < ans:
        ans = temp_dis

print(ans)