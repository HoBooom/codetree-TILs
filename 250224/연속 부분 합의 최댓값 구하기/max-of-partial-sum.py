import sys

INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

prefix_list = []

ans = INT_MIN
temp = 0
for i in range(len(arr)):
    temp += arr[i]
    prefix_list.append(temp)

idx1= prefix_list[0]

for i in range(1,len(prefix_list)):
    if i == 0:
        ans = max(prefix_list[i],ans)
    else:
        ans = max((prefix_list[i] - idx1),ans)
        if prefix_list[i] < idx1:
            idx1 = prefix_list[i]

print(ans)

