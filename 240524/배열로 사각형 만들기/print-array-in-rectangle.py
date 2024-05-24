list0 = [
    [1 for _ in range(5)]
    for _ in range(5)
]

for row in range(1,5):
    for column in range(1,5):
        list0[row][column] = list0[row - 1][column] + list0[row][column - 1]
    
for row in range(5):
    for column in range(5):
        print(list0[row][column],end= " ")
    print()