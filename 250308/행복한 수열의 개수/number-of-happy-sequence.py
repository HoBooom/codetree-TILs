n, m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

def check_r(i):
    row = board[i]
    sequence = 1
    temp_num = row[0]
    for r in range(1,n):
        if row[r] == temp_num:
            sequence += 1
        else:
            temp_num = row[r]
            sequence = 1
        if sequence >= m:
            return True
    return False

def check_c(i):
    column = []
    for j in range(n):
        column.append(board[j][i])
    sequence = 1
    temp_num = column[0]
    for c in range(1,n):
        if column[c] == temp_num:
            sequence += 1
        else:
            temp_num = column[c]
            sequence = 1
        if sequence >= m:
            return True
    return False
    
        
ans = 0

for i in range(n):
    if check_r(i):
        #print(f'r : {i}')
        ans += 1
    if check_c(i):
        ans += 1
        #print(f'c : {i}')

print(ans)
    