n = int(input())

# 각 위치 폭탄 종류 저장 -> 변함
# 0이면 폭탄 x, 1~3이면 해당 폭탄
bomb_type = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# T,F로 해당 위치 터졌는지 여부 확인 -> 변함
bombed = [
    [False for _ in range(n)]
    for _ in range(n)
]

# 최대값
ans = 0

# 각 폭탄의 위치 -> 안변함
bomb_pos = list()

def is_range(r,c):
    return 0 <= r < n and 0 <= c < n

def bomb(r,c, bomb_type): #특정 위치 폭탄 터트리기
    bomb_shape = [
        [],
        [[-2,0],[-1,0],[0,0],[1,0],[2,0]],
        [[-1,0],[1,0],[0,0],[0,-1],[0,1]],
        [[-1,-1],[-1,1],[0,0],[1,-1],[1,1]]
    ]

    for i in range(5):
        dr, dc = bomb_shape[bomb_type][i]
        nr, nc = r + dr, c + dc
        if is_range(nr,nc):
            bombed[nr][nc] = True
    
def calc(): 
    for i in range(n):
        for j in range(n):
            bombed[i][j] = False

    for i in range(n):
        for j in range(n):
            if bomb_type[i][j]:
                bomb(i,j,bomb_type[i][j])

    cnt = 0
    for i in range(n):
        for j in range(n):
            if bombed[i][j]:
                cnt += 1
    
    return cnt

def find_max_area(cnt):
    global ans

    if cnt == len(bomb_pos):
        ans = max(ans,calc())
        return
    
    for i in range(1,4):
        r,c = bomb_pos[cnt]
        
        bomb_type[r][c] = i
        find_max_area(cnt + 1)
        bomb_type[r][c] = 0

for i in range(n):
    given_row = list(map(int,input().split()))
    for j, bomb_place in enumerate(given_row):
        if bomb_place:
            bomb_pos.append((i,j))

find_max_area(0)

print(ans)


