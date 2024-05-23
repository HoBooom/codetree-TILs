n = int(input())

list0 = [
    [0 for _ in range(n)]
    for _ in range(n)
]

current = 1

for row in range(n):
    for column in range(n):
        list0[column][row] = current
        current+=1

for i in range(n):
    for j in range(n):
        print(list0[i][j],end=" ")
    print()