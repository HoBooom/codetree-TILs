n, m, k = map(int,input().split())

jumps = list(map(int,input().split())) #n

balls = [1 for _ in range(k)]

ans = 0

def check(balls):
    count = 0
    for ball in balls:
        if ball == m:
            count += 1
    return count

def program(cnt_n):
    global ans

    if cnt_n == n:
        ans = max(ans,check(balls))
        #print(balls,ans)
        return 
    
    for i in range(k):
        next_jump = jumps[cnt_n]
        if next_jump + balls[i] > m:
            next_jump = m - balls[i] 
        balls[i] += next_jump
        program(cnt_n + 1)
        balls[i] -= next_jump
        

program(0)

print(ans)

