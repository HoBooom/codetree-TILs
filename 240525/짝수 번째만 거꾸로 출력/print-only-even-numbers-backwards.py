arr = input()

new_a = []

for i in range(len(arr)):
    if i % 2 != 0:
        new_a.append(arr[i])
for i in range(len(new_a)):
    print(new_a.pop(),end="")