n = int(input())

x,y=0,0

dxs = [1,-1,0,0]
dys = [0,0,-1,1]

ans = -1
elapsed_time = 0

def move(move_dir, dist):
    global x,y
    global ans,elapsed_time

    for _ in range(dist):
        x,y = x + dxs[move_dir],y + dys[move_dir]
        elapsed_time += 1
        
        if x==0 and y==0:
            ans = elapsed_time
            return True
    return False


for _ in range(n):
    command,dist = input().split()
    dist = int(dist)
    if command == "E":
        move_dir = 0
    elif command =="W":
        move_dir = 1
    elif command =="S":
        move_dir = 2
    elif command =="N": 
        move_dir = 3
    done = move(move_dir,dist)
    
    if done:
        break
print(ans)