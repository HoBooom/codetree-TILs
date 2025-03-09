board = [list(map(int,input().split())) for _ in range(4)]

direct = input()

def shift(arr):
    temp = []
    for i in range(4):
        if arr[i] != 0:
            temp.append(arr[i])
    
    temp = temp + ([0] * (4 - len(temp)))
    return temp

def boom(arr):
    for i in range(1,4):
        if arr[i] == arr[i - 1]:
            arr[i - 1] = arr[i - 1] * 2
            arr[i] = 0
    return arr

def logic(arr):
    arr = shift(arr)
    arr = boom(arr)
    arr = shift(arr)
    return arr


if direct == 'R':
    for i in range(4):
        temp_arr = list(reversed(board[i]))
        temp_arr = logic(temp_arr)
        board[i] = list(reversed(temp_arr))
elif direct == 'L':
    for i in range(4):
        temp_arr = logic(board[i])
        board[i] = temp_arr
elif direct == 'U':
    for c in range(4):
        temp_arr = []
        for r in range(4):
            temp_arr.append(board[r][c])
        temp_arr = logic(temp_arr)
        for r in range(4):
            board[r][c] = temp_arr[r]
elif direct == 'D':
    for c in range(4):
        temp_arr = []
        for r in reversed(range(4)):
            temp_arr.append(board[r][c])
        temp_arr = logic(temp_arr)
        for i in range(4):
            board[3 - i][c] = temp_arr[i]

for r in range(4):
    print(*board[r])






