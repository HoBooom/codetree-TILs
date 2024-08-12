MAX_K = 1000

board = [
    [0 for _ in range(2*MAX_K + 1)] for _ in range(2*MAX_K + 1)
]


x1,y1,x2,y2 = map(int,input().split())
x1 += MAX_K
x2 += MAX_K
y1 += MAX_K
y2 += MAX_K
for x in range(x1,x2 + 1):
    for y in range(y1,y2 + 1):
        board[x][y] = 1

a1,b1,a2,b2 = map(int,input().split())
a1 += MAX_K
a2 += MAX_K
b1 += MAX_K
b2 += MAX_K
for a in range(a1,a2 + 1):
    for b in range(b1,b2 + 1):
        board[a][b] = 0

count = 0

for x in range(2 * MAX_K + 1):
    for y in range(2 * MAX_K + 1):
        if board[x][y] == 1:
            count += 1
print(count)