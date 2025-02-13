n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

###
ans = 0

for r in range(n):
    for c in range(n - 2):
        block = arr[r][c] + arr[r][c + 1] + arr[r][c + 2]
        for row in range(n):
            for col in range(n - 2):
                if r == row and c - 2 <= col <= c + 2:
                    continue
                block2 = arr[row][col] + arr[row][col + 1] + arr[row][col + 2]
                if block + block2 > ans:
                    ans = block + block2

print(ans)

        


