N, M, K = map(int, input().split())


# Write your code here!

punish = [0]*(N + 1)
isAns = False

def check(punish):
    for i,item in enumerate(punish):
        if item >= K:
            return i
    return -1

for _ in range(M):
    student = int(input())
    punish[student - 1] += 1
    if check(punish) != -1:
        isAns = True
        break

if not isAns:
    print(-1)
else:
    print(check(punish) + 1)


