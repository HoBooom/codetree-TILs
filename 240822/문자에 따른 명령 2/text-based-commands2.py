command = input()
commands = list(command)

x = y = 0
cnt_d = 3

dx = [1,0,-1,0]
dy = [0,-1,0,1]

for i,v in enumerate(commands):
    if v == "L":
        cnt_d = (cnt_d + 3) % 4
    elif v == "R":
        cnt_d = (cnt_d + 1) % 4
    elif v == "F":
        x = x + dx[cnt_d]
        y = y + dy[cnt_d]
    
print(x,y)