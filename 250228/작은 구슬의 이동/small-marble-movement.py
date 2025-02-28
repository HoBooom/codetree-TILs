n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.

def is_range(r,c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False

dr,dc = [0,1,0,-1],[1,0,-1,0]

dir_n = {
    'R' : 0,
    'D' : 1,
    'L' : 2,
    'U' : 3,
}

dir_num = dir_n[d]
r -= 1
c -= 1
for i in range(t):
    nr,nc = r + dr[dir_num],c + dc[dir_num]
    if is_range(nr,nc):
        r,c = nr,nc
    else:
        dir_num = (dir_num + 2) % 4

print(r + 1,c + 1)