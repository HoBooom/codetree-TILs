N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Write your code here!


def is_range(r,c):
    if 0<=r<N and 0<=c<M:
        return True
    return False

def make_str(r,c,dr,dc):
    temp=[]
    temp.append(arr[r][c])
    for _ in range(2):
        nr,nc = r + dr,c + dc
        if is_range(nr,nc):
            temp.append(arr[nr][nc])
            r,c = nr,nc
        else:
            break
    temp_str = ''.join(temp)
    return temp_str



def isLee(r,c):
    count = 0
    dr,dc = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]
    for dir_num in range(8):
        temp_str = make_str(r,c,dr[dir_num],dc[dir_num])
        if temp_str == 'LEE':
            count += 1
    return count

ans = 0
for r in range(N):
    for c in range(M):
        ans += isLee(r,c)

print(ans)
        

        