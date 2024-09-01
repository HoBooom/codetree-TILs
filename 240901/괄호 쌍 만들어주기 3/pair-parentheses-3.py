comment = list(input())

length = len(comment)

count = 0

for i in range(length):
    if comment[i] == '(':
        for j in range(i + 1, length):
            if comment[j] == ')':
                count += 1

print(count)