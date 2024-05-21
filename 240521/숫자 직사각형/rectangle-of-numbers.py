row, column = map(int,input().split())

matrix =[]

current = 1

for i in range(row):
    temp = []
    for j in range(column):
        temp.append(current)
        current += 1
    matrix.append(temp)


for items in matrix:
    for item in items:
        print(item,end=" ")
    print()