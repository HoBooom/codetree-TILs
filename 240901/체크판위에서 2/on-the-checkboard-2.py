r,c = map(int,input().split())

board = [
    list(input().split()) for _ in range(r)
]


def func_jump1(r,c):
    cases_count = 0
    if board[0][0] == 'W':
        for row in range(1,r-2):
            for column in range(1,c-2):
                if board[row][column] == 'B':
                    cases_count += func_jump2(row,column)
    elif board[0][0] == 'B':
        for row in range(1,r-2):
            for column in range(1,c-2):
                if board[row][column] == 'W':
                    cases_count += func_jump2(row,column)
    return cases_count

def func_jump2(r1,c1):
    count = 0
    if board[r1][c1] == 'W':
        for row in range(r1 + 1, r - 1):
            for column in range(c1 + 1, c - 1):
                if board[row][column] =='B':
                    count += 1
    elif board[r1][c1] == 'B':
        for row in range(r1 + 1, r - 1):
            for column in range(c1 + 1, c - 1):
                if board[row][column] =='W':
                    count += 1
    return count

ans = func_jump1(r,c)
if board[0][0] == board[r- 1][c - 1]:
    ans = 0
print(ans)