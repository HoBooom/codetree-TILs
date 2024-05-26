index = -1

context = input()
find = input()
temp = len(find)

for i in range(len(context)):
    if context[i:i + temp] == find:
        index = i
        break
print(index)