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

    if cur_idx == n - 1:
        if info[cnt][0] == 0:
            return
        cnt_cost = sum(cost) + info[cnt][0]
        #print(cnt, cost)
        ans = min(ans, cnt_cost)
        return


    for i in range(1,n):
        if info[cnt][i] == 0:
            continue
        if visited[i]:
            continue
        
        visited[i] = True
        cost.append(info[cnt][i])
        find(cur_idx + 1, i)

        visited[i] = False
        cost.pop()

    return

find(0,0)

print(ans)