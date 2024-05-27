def switch_chairs(n, k, commands):
    # 초기 설정: 각 사람이 자신의 번호에 해당하는 자리에 앉아 있음
    men_in_chair = [i for i in range(n)]
    men_move = [[] for _ in range(n)]
    
    for i in range(n):
        men_move[i].append(i)

    # 자리 바꾸기 명령 반복 적용
    for _ in range(3):
        for a, b in commands:
            a -= 1
            b -= 1
            men_in_chair[a], men_in_chair[b] = men_in_chair[b], men_in_chair[a]

            if b not in men_move[men_in_chair[a]]:
                men_move[men_in_chair[a]].append(b)
            if a not in men_move[men_in_chair[b]]:
                men_move[men_in_chair[b]].append(a)
    
    # 각 사람이 앉을 수 있는 자리의 개수 출력
    for i in range(n):
        print(len(men_move[i]))

# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
commands = []

index = 2
for _ in range(k):
    a = int(data[index])
    b = int(data[index + 1])
    commands.append((a, b))
    index += 2

switch_chairs(n, k, commands)