board = [list(map(int, input().split())) for _ in range(19)]

# Write your code here!

def is_range(r,c):
    if 0<=r<19 and 0<=c<19:
        return True
    return False

def make_line(r,c,dr,dc):
    line = []
    line.append(board[r][c])
    for _ in range(4):
        nr,nc = r + dr,c + dc
        if is_range(nr,nc):
            line.append(board[nr][nc])
            r,c = nr,nc
        else:
            break 
    #print(line)
    return line


def isWin(r,c):
    #오른쪽 부터 한바퀴
    dr,dc=[0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]
    
    for dir_num in range(8):
        temp_line = make_line(r,c,dr[dir_num],dc[dir_num])
        if len(temp_line) == 5:
            isdifferent = False
            for i in range(4):
                if temp_line[i] != temp_line[i + 1]:
                    isdifferent = True
                    break
            if not isdifferent: # 5칸이 모두 같으면
                #print(temp_line)
                return (r + 2*dr[dir_num],c + 2*dc[dir_num])
    return (-1,-1)

                
ans_r,ans_c = (-1,-1)

for r in range(19):
    isEnd = False
    for c in range(19):
        #print(f"r c : {r} {c}")
        if board[r][c] != 0:
            temp_r,temp_c = isWin(r,c)
            if (temp_r,temp_c) != (-1,-1):
                isEnd = True
                ans_r,ans_c = temp_r,temp_c
                break
    if isEnd:
        break

if (ans_r,ans_c) != (-1,-1):
    print(board[ans_r][ans_c])
    print(ans_r + 1,ans_c + 1)
else:
    print(0)
            



