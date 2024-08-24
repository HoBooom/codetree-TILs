command = input()
commands = list(command)
#print(commands)

time = 0
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

direct = 0
x,y=0,0

ans = -1

for i,c in enumerate(commands):
    #print(c)
    if c == "F":
        x,y = x + dxs[direct], y + dys[direct]
        time += 1
    elif c =="L":
        direct = (direct + 3)%4
        time += 1
    elif c=="R":
        direct = (direct + 1)%4
        time += 1
    
    if x == 0 and y == 0:
        ans = time
        break

print(ans)