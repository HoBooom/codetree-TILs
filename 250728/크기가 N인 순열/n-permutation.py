N = int(input())

nums = []

is_visited = [False] * (N + 1)


def choose(cur_idx):
    if cur_idx == N + 1:
        print(*nums)
        return
    
    for i in range(1, N + 1):
        if not is_visited[i]:
            nums.append(i)
            is_visited[i] = True
            choose(cur_idx + 1)
            nums.pop()
            is_visited[i] = False

    return

choose(1)


