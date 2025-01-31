N, M, K = map(int, input().split())


# Write your code here!

punish = [0]*N

def check(punish):
    for i,item in enumerate(punish):
        if item >= K:
            return i
    return -1

for _ in range(M):
    student = int(input())
    punish[student - 1] += 1
    if check(punish) != -1:
        break

print(check(punish) + 1)

