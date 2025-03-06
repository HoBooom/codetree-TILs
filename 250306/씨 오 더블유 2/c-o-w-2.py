n = int(input())
string = list(input())

ans = 0

for i in range(n):
    if string[i] == 'C':
        for j in range(i + 1, n):
            if string[j] == 'O':
                for k in range(j + 1, n):
                    if string[k] == 'W':
                        ans += 1

print(ans)