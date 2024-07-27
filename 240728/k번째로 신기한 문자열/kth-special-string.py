n,k,t = map(str,input().split())
n = int(n)
k = int(k)
t = list(t)

strings = []

for _ in range(n):
    check = 0
    temp = list(input())
    for i in range(len(t)):
        if t[i] != temp[i]:
            check = 1
            break
    if check == 1:
        continue
    else:
        strings.append(''.join(temp))

strings.sort()

print(strings[k - 1])