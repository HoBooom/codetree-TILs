n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Write your code here!

cnt_r,cnt_c = 0,-1

def is_range(r,c):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False



dir_num = 0

dr,dc = [0,1,0,-1],[1,0,-1,0]

cnt_num = 1

while True:
    n_r,n_c = cnt_r + dr[dir_num],cnt_c + dc[dir_num]
    if is_range(n_r,n_c) and arr[n_r][n_c] == 0:
        arr[n_r][n_c] = cnt_num
        if cnt_num == n*m:
            break
        cnt_r,cnt_c = n_r,n_c
        cnt_num += 1
    else:
        dir_num = (dir_num + 1) % 4
        
    
    
    


    

for _,r in enumerate(arr):
    for _,c in enumerate(r):
        print(c,end=" ")
    print()
    
   
