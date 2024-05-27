def switch_chair(men_move, men_in_chair, commend_a, commend_b, k):
    for i in range(k):
        ca = commend_a[i]  # 명령 a
        cb = commend_b[i]  # 명령 b
        men_A = men_in_chair[ca]  # ca 위치의 남자
        men_B = men_in_chair[cb]  # cb 위치의 남자
        men_in_chair[ca], men_in_chair[cb] = men_in_chair[cb], men_in_chair[ca]

        if cb not in men_move[men_A]:
            men_move[men_A].append(cb)
        if ca not in men_move[men_B]:
            men_move[men_B].append(ca)

    return men_move, men_in_chair

n, k = map(int, input().split())

men_in_chair = [i for i in range(n)]

commend_a = []
commend_b = []

for i in range(k):
    a, b = map(int, input().split())
    commend_a.append(a - 1)
    commend_b.append(b - 1)

men_move = [[] for _ in range(n)]
for i in range(n):
    men_move[i].append(i)

# 명령을 세 번 반복하는 대신 모든 이동 경로를 정확하게 기록하도록 수정
for _ in range(3):
    for i in range(k):
        ca = commend_a[i]
        cb = commend_b[i]
        men_A = men_in_chair[ca]
        men_B = men_in_chair[cb]
        men_in_chair[ca], men_in_chair[cb] = men_in_chair[cb], men_in_chair[ca]

        if cb not in men_move[men_A]:
            men_move[men_A].append(cb)
        if ca not in men_move[men_B]:
            men_move[men_B].append(ca)

for i in range(n):
    print(len(men_move[i]))