import sys

INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

prefix_list = []

def pre_min(i):
    temp = - INT_MIN
    for i in range(i):
        if prefix_list[i] < temp:
            temp = prefix_list[i]
    return temp
ans = INT_MIN
temp = 0
for i in range(len(arr)):
    temp += arr[i]
    prefix_list.append(temp)

for i in range(len(prefix_list)):
    ans = max((prefix_list[i] - pre_min(i)),ans)

print(ans)
