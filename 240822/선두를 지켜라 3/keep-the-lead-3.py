n,m = map(int,input().split())

a_moves = []
b_moves = []
a_moves.append(0)
b_moves.append(0)

cnt_a = 0
for _ in range(n):
    v,t = map(int,input().split())
    for _ in range(t):
        cnt_a += v
        a_moves.append(cnt_a)
    
cnt_b = 0
for _ in range(m):
    v,t = map(int,input().split())
    for _ in range(t):
        cnt_b += v
        b_moves.append(cnt_b)

#print(a_moves)
#print(b_moves)

cnt_pos = -1 #둘다 선두 0, a가 선두 1, b가 선두 2
count = 0

time = len(a_moves)

temp = -1

for i in range(1,time):
    if a_moves[i] == b_moves[i]:
        temp = 0
    elif a_moves[i] > b_moves[i]:
        temp = 1
    elif a_moves[i] < b_moves[i]:
        temp = 2
    #print(a_moves[i],b_moves[i],temp,cnt_pos,count)
    
    if temp != cnt_pos:
        count += 1
    cnt_pos = temp

print(count)