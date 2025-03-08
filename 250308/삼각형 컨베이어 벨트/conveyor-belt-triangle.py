n,t = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

def push(row):
    temp = row[-1]
    for i in reversed(range(1,len(row))):
        row[i] = row[i - 1]
    return row,temp


for _ in range(t):
    temp_list = []
    for i in range(n):
        temp = 0
        board[i],temp = push(board[i])
        temp_list.append(temp)
    
    for i in range(n):
        if i == 0:
            board[i][0] = temp_list[-1]
        else:
            board[i][0] = temp_list[i - 1]

for _,item in enumerate(board):
    print(*item)