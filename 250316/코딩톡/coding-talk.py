N, M, P = map(int,input().split())

message = []
for _ in range(M):
    man, count = input().split()
    message.append((man,int(count)))

all_man = []
for i in range(N):
    all_man.append(chr(ord("A") + i))

after_p = message[P - 1:]
for _,(m,n) in enumerate(after_p):
    if m in all_man:  # 리스트에 있는 경우만 제거
        all_man.remove(m)
#print(*all_man)

if message[P - 1][1] == 0:
    print()
else:
    print(*all_man)