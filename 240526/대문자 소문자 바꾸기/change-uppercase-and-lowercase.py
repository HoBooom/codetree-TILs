s = input()

new = []

for i in range(len(s)):
    #소문자이면
    if ord(s[i]) >= ord('a'):
        new.append(s[i].upper())
    else:
        new.append(s[i].lower())

new = ''.join(new)

print(new)