string = list(input())
#print(string)

ans = 0

for i in range(len(string)):
    if string[i] == '(':
        for j in range(i + 1,len(string)):
            if string[j] == ')':
                ans += 1
    else:
        continue

print(ans)