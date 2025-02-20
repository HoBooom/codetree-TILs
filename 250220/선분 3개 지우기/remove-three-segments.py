n = int(input())

line = [0] * 101
command = []
for _ in range(n):
    x0,x1 = map(int,input().split())
    command.append((x0,x1))

def f(command):
    board = [0]*101
    for _,(x0,x1) in enumerate(command):
        for i in range(x0,x1 + 1):
            if x1 == 0:
                continue
            board[i] += 1
    if max(board) > 1:
        #print(board)
        return False
    return True

ans = 0
for i in range(n):
    for j in range(i + 1,n):
        for k in range(j + 1,n):
            temp_command = command[:]
            temp_command[i] = temp_command[j] = temp_command[k] = (0,0)
            #print(temp_command)
            if f(temp_command):
                ans += 1
                #print('check')

print(ans)

                
            
            


