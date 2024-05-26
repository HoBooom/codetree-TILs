s = input()

ans =[]


for i in range(len(s)):
    if s[i].isalpha():
        ans.append(s[i])

ans = ''.join(ans)

print(ans.upper())