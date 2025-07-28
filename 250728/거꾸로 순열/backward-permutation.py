n = int(input())

visited = [False] * (n + 1)

nums = []

def choose(cnt):
    if cnt == n + 1:
        print(*nums)
        return
    
    for i in reversed(range(1, n + 1)):
        if visited[i]:
            continue
        
        nums.append(i)
        visited[i] = True
        choose(cnt + 1)

        nums.pop()
        visited[i] = False
    
    return

choose(1)