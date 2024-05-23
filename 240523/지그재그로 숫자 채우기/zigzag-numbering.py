rows, columns = map(int,input().split())

list0 = [
    [0 for _ in range(columns)]
    for _ in range(rows)
]

current = 0


for column in range(columns):
    for row in range(rows):
        if column % 2 == 0:
            list0[row][column] = current
            current += 1
        else:
            list0[3 - row][column] = current
            current += 1

for i in range(rows):
    for j in range(columns):
        print(list0[i][j],end=" ")
    print()