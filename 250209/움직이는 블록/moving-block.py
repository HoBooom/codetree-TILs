n = int(input())
blocks = [int(input()) for _ in range(n)]

# Write your code here!

make = sum(blocks) // n

move = 0

for point in (blocks):
    if point < make:
        move += make - point

print(move)
