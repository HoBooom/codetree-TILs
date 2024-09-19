import sys

INT_MIN = -sys.maxsize

n,k = map(int,input().split())

baskets = []

for _ in range(n):
    candy, place = map(int,input().split())
    baskets.append((candy,place))

baskets.sort(key = lambda x : x[1])

first_place = baskets[0][1]
last_place = baskets[n - 1][1] # 15


ans = INT_MIN


for i in range(first_place + k, last_place - k + 1):
    temp = 0
    f_index = i - k
    l_index = i + k

    
    for j in range(n):
        if f_index <= baskets[j][1] <= l_index:
            temp += baskets[j][0]
    ans = max(ans,temp)

if first_place == last_place:
    ans = 0
    for i in range(n):
        ans = baskets[i][0]

print(ans)