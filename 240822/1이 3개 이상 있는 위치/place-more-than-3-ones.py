n =int(input())

board = [
   [0 for _ in range(n)] for _ in range(n)
]

count = 0 

for i in range(n):
    temp = list(map(int,input().split()))
    board[i] = temp


        

def check(x,y,board,n):
    temp = 0
    #동
    if x + 1 < n:
        if board[x + 1][y] == 1:
            temp += 1
    #서
    if x - 1 >= 0:
        if board[x - 1][y] == 1:
            temp += 1
    #남
    if y + 1 < n:
        if board[x][y + 1] == 1:
            temp += 1
    #북
    if y - 1 >=0:
        if board[x][y - 1] == 1:
            temp += 1

    if temp >=3:
        return True
    else:
        return False

for x in range(n):
    for y in range(n):
        if check(x,y,board,n) == True:
            count += 1
print(count)