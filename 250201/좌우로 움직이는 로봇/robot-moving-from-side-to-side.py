n, m = map(int, input().split())

# Process robot A's movements
a_position = []
a_position.append(0)
a_cnt = 0

for _ in range(n):
    time,direction = input().split()
    time = int(time)
    if direction == 'R':
        for _ in range(time):
            a_cnt += 1
            a_position.append(a_cnt)
    elif direction == 'L':
        for _ in range(time):
            a_cnt -= 1
            a_position.append(a_cnt)

# Process robot B's movements
b_position = []
b_position.append(0)
b_cnt = 0

for _ in range(m):
    time,direction = input().split()
    time = int(time)
    if direction == 'R':
        for _ in range(time):
            b_cnt += 1
            b_position.append(b_cnt)
    elif direction == 'L':
        for _ in range(time):
            b_cnt -= 1
            b_position.append(b_cnt)

# Write your code here!

def is_different(a_pos,b_pos):
    if a_pos != b_pos:
        return True
    return False

def isEnd(i,a_position):
    if i >= len(a_position):
        return True
    return False

was_different = is_different(a_position[0],b_position[0])

ans = 0

for i in range(max(len(a_position),len(b_position))):
    a_idx = i
    b_idx = i
    if isEnd(i,a_position):
        a_idx = len(a_position) - 1
    if isEnd(i,b_position):
        b_idx = len(b_position) - 1

    cnt_different = is_different(a_position[a_idx],b_position[b_idx])
    if was_different and not cnt_different:
        ans += 1
    was_different = cnt_different

#print(a_position)
#print(b_position)
print(ans)
