n = int(input())
jenga = [int(input()) for _ in range(n)]

a1,b1 = map(int,input().split())
a2,b2 = map(int,input().split())

temp_jenga = []
for i in range(n):
    if a1 - 1 <= i < b1:
        continue
    temp_jenga.append(jenga[i])
#print(*temp_jenga)

ans_jenga = []
for i in range(len(temp_jenga)):
    if a2 - 1 <= i < b2:
        continue
    ans_jenga.append(temp_jenga[i])

print(len(ans_jenga))
for i in range(len(ans_jenga)):
    print(ans_jenga[i])

