N = int(input())

# Write your code here!

first_x,first_y = 0,0

cnt_x,cnt_y = 0,0

order = {
    'E' : 0,
    'S' : 1,
    'W' : 2,
    'N' : 3,
}

dx,dy = [1,0,-1,0],[0,-1,0,1]

ans = -1
count = 0

commands = []

for _ in range(N):
    di,xi = input().split()
    commands.append((di,int(xi)))

for _,(di,xi) in enumerate(commands):
    for t in range(xi):
        cnt_x,cnt_y = cnt_x + dx[order[di]], cnt_y + dy[order[di]]
        count += 1
        #print(cnt_x,cnt_y,count)
        if cnt_x == first_x and cnt_y == first_y:
            ans = count
            break

print(ans)
        
