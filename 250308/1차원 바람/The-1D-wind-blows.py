N, M, Q = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

order = [tuple(input().split()) for _ in range(Q)]

def shift(arr, wind):
    if wind == 'L':
        temp = arr[-1]
        for i in reversed(range(1,len(arr))):
            arr[i] = arr[i - 1]
        arr[0] = temp
        return arr
    else:
        temp = arr[0]
        for i in range(len(arr) - 1):
            arr[i] = arr[i + 1]
        arr[-1] = temp
        return arr
    

for _,(row,wind) in enumerate(order):
    r = int(row) - 1
    board[r] = shift(board[r],wind)
    before = board[r]
    before_dir = wind
    is_change = False
    for i in reversed(range(r)):
        for j in range(M):
            if before[j] == board[i][j]:
                is_change = True
                break
        if is_change and before_dir == 'L':
            board[i] = shift(board[i],'R')
            before = board[i]
            before_dir = 'R'
            is_change = False
        elif is_change and before_dir == 'R':
            board[i] = shift(board[i],'L')
            before = board[i]
            before_dir = 'L'
            is_change = False
        else:
            break
    before = board[r]
    before_dir = wind
    is_change = False

    for i in range(r + 1, N):
        for j in range(M):
            if before[j] == board[i][j]:
                is_change = True
                break
        if is_change and before_dir == 'L':
            board[i] = shift(board[i],'R')
            before = board[i]
            before_dir = 'R'
            is_change = False
        elif is_change and before_dir == 'R':
            board[i] = shift(board[i],'L')
            before = board[i]
            before_dir = 'L'
            is_change = False
        else:
            break

for r in range(N):
    print(*board[r])
        
        

