n,m,k = map(int,input().split())

grid = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    apple_r,apple_c = map(int,input().split())
    grid[apple_r - 1][apple_c - 1] = 1

commands = [tuple(map(str,input().split())) for _ in range(k)]

def is_range(r,c):
    return 0<=r<n and 0<=c<n

class Node:
    def __init__(self,r,c):
        self.r = r
        self.c = c
    
    def move(self,r,c,command):
        if command == 'U':
            self.r,self.c = r - 1, c
        elif command == 'D':
            self.r,self.c = r + 1, c
        elif command == 'L':
            self.r,self.c = r, c - 1
        elif command == 'R':
            self.r,self.c = r, c + 1
        
    def follow(self,nr,nc):
        self.r = nr
        self.c = nc
    
    def cnt_pos(self):
        return (self.r,self.c)

class Snake:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.bodys = [self.head, Node(0,0), self.tail]
        self.length = len(self.bodys)
        self.is_end = False
    
    def eat(self,r,c):
        new_node = Node(r,c)
        self.bodys.append(new_node)
        self.tail = new_node
        self.length += 1
    
    def move(self,command):
        nr,nc = self.head.cnt_pos()
        last_r,last_c = self.tail.cnt_pos()

        self.head.move(nr,nc,command)
        h_r,h_c = self.head.cnt_pos()

        if self.accident(h_r,h_c) or not is_range(h_r,h_c):
            self.is_end = True
            return

        prev_pos = []
        for b in self.bodys:
            prev_pos.append(b.cnt_pos())
        
        for i in range(1,self.length):
            self.bodys[i].follow(*prev_pos[i-1])
        
        
        if grid[h_r][h_c] == 1:
            self.eat(last_r,last_c)
            grid[h_r][h_c] = 0

    
    def accident(self,h_r,h_c):
        for i in range(1,len(self.bodys)):
            cnt_r,cnt_c = self.bodys[i].cnt_pos()
            if h_r == cnt_r and h_c == cnt_c:
                return True
        return False

snake = Snake()

time = 0
for (dir_command, len_command) in commands:
    len_command = int(len_command)
    is_over = False

    for _ in range(len_command):
        snake.move(dir_command)
        time += 1
        if snake.is_end == True:
            is_over = True
            break

    if is_over:
        break

print(time)

