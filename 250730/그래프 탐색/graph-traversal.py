n, m = map(int,input().split())

edges = [
    tuple(map(int,input().split())) for _ in range(m)
]

# graph = [[0 for _ in range(n)] for _ in range(n)]

visited = [False] * (n + 1)
visited[1] = True

count = 0

# for edge in edges:
#     x, y = edge
#     graph[x - 1][y - 1] = 1
#     graph[y - 1][x - 1] = 1

def dfs(vertex):
    global count 
    for (x,y) in edges:
        if x == vertex and not visited[y]:
            visited[y] = True
            count += 1
            dfs(y)
        if y == vertex and not visited[x]:
            visited[x] = True
            count += 1
            dfs(x)
    return

dfs(1)

print(count)

