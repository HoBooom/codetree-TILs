n,m = map(int,input().split())

list0=[
    [0 for _ in range(n)]
    for _ in range(n)
]

sequence = 1

for _ in range(m):
    r,c = map(int,input().split())
    list0[r-1][c-1] = sequence
    sequence +=1

for i in range(n):
    for j in range(n):
        print(list0[i][j],end=" ")
    print()