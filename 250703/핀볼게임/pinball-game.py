n = int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

def is_range(r,c):
    return 0<=r<n and 0<=c<n

def input_ball(r,c,direct):
    drs,dcs = [-1,0,1,0],[0,-1,0,1]
    if not is_range(r,c):
        return 0
    if grid[r][c] == 1: # / 0 -> 3, 3 -> 0, 1 -> 2, 2 -> 1
        direct = (3 - direct)
    elif grid[r][c] == 2: # \ 0 -> 1, 1 -> 0, 2 -> 3, 3 -> 2
        if direct == 0:
            direct = 1
        elif direct == 1:
            direct = 0
        elif direct == 2:
            direct = 3
        elif direct == 3:
            direct = 2
    nr,nc = r + drs[direct],c + dcs[direct]
    return input_ball(nr,nc,direct) + 1
    


# 만약 방향이 / 인경우
#필요한 정보 현재 위치(r,c),방향dir
ans = 0
#1행, n행 input
for c in range(n):
    #위에서 부터
    temp_t1 = input_ball(0,c,2)
    temp_t2 = input_ball(n-1,c,0)
    ans = max(ans,temp_t1,temp_t2)
    #print(f"c: {c}, ans :{ans}, t1 {temp_t1}, t2 {temp_t2}")

for r in range(n):
    temp_t3 = input_ball(r,0,3)
    temp_t4 = input_ball(r,n-1,1)
    ans = max(ans,temp_t3,temp_t4)
    #print(f"r: {r}, ans :{ans}, t3 {temp_t3}, t4 {temp_t4}")

print(ans+1)

