size = int(input())

items = list(map(int, input().split()))

for i in range(size):
    for j in range(0, size - i - 1):
        if items[j] > items[j + 1]:
            items[j], items[j + 1] = items[j + 1], items[j]

for i in range(size):
    print(f"{items[i]}",end=" ")