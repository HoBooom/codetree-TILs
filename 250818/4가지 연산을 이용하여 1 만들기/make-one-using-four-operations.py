from collections import deque

N = int(input())

# Please write your code here.

#최대를 그냥 1을 계속 빼는걸로 놓고 풀면 될듯

threshold = N - 1
ans = threshold

q = deque()
q.append((N,0))

while q:
    cnt_num,cnt_depth = q.pop()
    if cnt_num == 1:
        ans = min(ans,cnt_depth)
        break
    if cnt_depth >= threshold:
        break
    
    for i in range(4):
        if i == 0:
            q.appendleft((cnt_num - 1, cnt_depth + 1))
        elif i == 1:
            q.appendleft((cnt_num + 1, cnt_depth + 1))
        elif i == 2:
            if cnt_num % 2 == 0:
                q.appendleft((cnt_num // 2, cnt_depth + 1))
        elif i == 3:
            if cnt_num % 3 == 0:
                q.appendleft((cnt_num // 3, cnt_depth + 1))

print(ans)


