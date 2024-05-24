n = int(input())

list0=[
    [-1 for _ in range(n)]
    for _ in range(n)
]

current = n*n

for column in range(n):
    if n % 2 == 0:
        if column % 2 == 0:
            for  row in reversed(range(n)):
                list0[row][column] = current
                current -= 1
        else:
            for row in range(n):
                list0[row][column] = current
                current -= 1
    else:
        if column % 2 != 0:
            for  row in reversed(range(n)):
                list0[row][column] = current
                current -= 1
        else:
            for row in range(n):
                list0[row][column] = current
                current -= 1


for i in range(n):
    for j in range(n):
        print(list0[i][j],end=" ")
    print()