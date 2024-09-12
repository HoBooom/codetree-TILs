import sys

INT_MIN = -sys.maxsize

ans = INT_MIN

n,k = map(int,input().split())

pic = []

for i in range(n):
    index, flag = input().split()
    index = int(index)

    pic.append((index,flag))

pic.sort(key = lambda x : x[0])

def get_point(alpha):
    if alpha == 'G':
        return 1
    else:
        return 2

for i in range(n):
    point = get_point(pic[i][1])

    j = i
    while True:
        if j + 1 < n and abs(pic[i][0] - pic[j + 1][0]) <= k:
            point += get_point(pic[j + 1][1])
        else:
            break
        j += 1
    
    ans = max(ans,point)

print(ans)