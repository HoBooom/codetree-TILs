n, m = map(int, input().split())

# 로봇 A와 B의 초기 위치
a_pos = 0
b_pos = 0

# 현재 시간을 나타내는 변수
a_time = 0
b_time = 0

# 만남 횟수 카운트
count = 0

# 로봇 A의 움직임 처리
a_moves = []
for _ in range(n):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        if d == 'L':
            a_pos -= 1
        else:
            a_pos += 1
        a_moves.append(a_pos)

# 로봇 B의 움직임 처리
b_moves = []
for _ in range(m):
    t, d = input().split()
    t = int(t)
    for _ in range(t):
        if d == 'L':
            b_pos -= 1
        else:
            b_pos += 1
        b_moves.append(b_pos)

# 로봇 A와 B의 최대 이동 시간 중 큰 값을 기준으로 반복
max_time = max(len(a_moves), len(b_moves))
a_pos = 0  # 초기 위치
b_pos = 0  # 초기 위치

for i in range(max_time):
    prev_a_pos = a_pos
    prev_b_pos = b_pos
    
    if i < len(a_moves):
        a_pos = a_moves[i]
    if i < len(b_moves):
        b_pos = b_moves[i]
    
    if a_pos == b_pos and prev_a_pos != prev_b_pos:
        count += 1

print(count)