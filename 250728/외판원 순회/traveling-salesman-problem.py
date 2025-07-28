import sys

INT_MAX = sys.maxsize

n = int(input())

info = [
    list(map(int,input().split())) for _ in range(n)
]

visited = [False] * n
visited[0] = True

cost = []

ans = INT_MAX

def find(cur_idx, cnt):
    global ans
    
    if cur_idx == n:
        cnt_cost = sum(cost) + info[cnt][0]
        ans = min(ans, cnt_cost)
        return


    for i in range(n):
        if visited[i]:
            continue
        
        visited[i] = True
        cost.append(info[cnt][i])
        find(cur_idx + 1, i)

        visited[i] = False
        cost.pop()

    return

find(1,0)

print(ans)