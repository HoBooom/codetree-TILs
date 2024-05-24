n = int(input())

list0=[
    [1 for _ in range(n)]
    for _ in range(n)
]

for i in range(1,5):
    for j in range(1,5):
        list0[i][j] = list0[i-1][j-1] + list0[i -1][j] + list0[i][j  - 1]

for i in range(5):
    for j in range(5):
        print(list0[i][j],end=" ")
    print()