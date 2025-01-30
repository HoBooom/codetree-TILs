n, k = map(int, input().split())

board = [0] * (n + 1)

commands = [tuple(map(int, input().split())) for _ in range(k)]


# Write your code here!


for i,item in enumerate(commands):
    for j in range(item[0],item[1] + 1):
        board[j] += 1

print(max(board))
