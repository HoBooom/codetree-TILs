import sys


n = int(input())

board = [
    list(map(int,input().split())) for _ in range(n)
]

count = 0

def area2(cnt_r,cnt_c,area1):
    
    area2 = 0

    max_area = area1 + area2

    for r in range(cnt_r,n):
        for c in range(cnt_c,n-2):
            if r == cnt_r and cnt_c - 2 <= c <= cnt_c + 2:
                continue
            area2 = board[r][c] + board[r][c + 1] + board[r][c + 2]
            max_area = max(max_area,area1 + area2)

    return max_area


ans = 0

for r in range(n):
    for c in range(n - 2):
        area1 = board[r][c] + board[r][c + 1] + board[r][c + 2]
        temp = area2(r,c,area1)
        
        ans = max(ans,temp)

print(ans)